from django.db import models

from .utils import cascade_archive


class SoftDeleteQuerySet(models.query.QuerySet):
    """
    QuerySet whose delete() does not delete items, but instead marks the
    rows as not active, and updates the timestamps
    """

    def delete(self):
        # doing an update is the most efficient, but does not promise
        # that the cascade will happen. E.g.
        # return self.update(deleted_on=timezone.now())

        # from django source
        # https://github.com/django/django/blob/1.8.6/django/db/models/query.py
        # Line:
        #   #L516
        assert self.query.can_filter(), \
            "Cannot use 'limit' or 'offset' with delete."

        # iterating and deleting ensures that the cascade delete will
        # occur for each instance.
        collector = cascade_archive(self.all(), self.db)
        self._result_cache = None
        return collector.delete()

    delete.alters_data = True

    def available(self):
        return self.filter(_deleted_at__isnull=True)


class SoftDeleteManager(models.Manager):
    """
    A model manager that defaults to using the ArchiveQuerySet such that
    the default queryset pre-excludes the "deleted" objects.

    A queryset with all objects, including any deleted objects, is available
    via the `deleted_qs` property.
    """

    def get_queryset(self):
        """
        Return a queryset without any deleted instances.
        """
        return SoftDeleteQuerySet(self.model, using=self._db).available()

    @property
    def deleted_qs(self):
        """
        Usage: MyModel.objects.deleted_qs.filter(...)

        Returns QuerySet: Queryset including deleted items.
        """
        return super(SoftDeleteManager, self).get_queryset().filter(_deleted_at__isnull=False)
