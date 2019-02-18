from django.db import models
from django.forms import model_to_dict

from . import managers
from .utils import cascade_archive


class SoftDeleteMixin(models.Model):
    """
    A model that is only marked as deleted when the .delete() method is called,
    instead of actually deleted. Calling .delete() on this object will only
    mark it as deleted, and it will not show up in the default queryset. If you
    want to see all objects, including the ones marked as deleted, use:

        ArchiveModel.objects.all_objects.all()

    If you want to just see the ones marked as deleted, use:

        ArchiveModel.objects.deleted.all()
    """
    _deleted_at = models.DateTimeField(null=True)

    objects = managers.SoftDeleteManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def get_candidate_relations_to_delete(self):
        """
        Returns
        """
        return models.deletion.get_candidate_relations_to_delete(self._meta)

    def related_objects(self, relation_field):
        """
        Given a relation field return the QuerySet of objects that are
        related to the current object (self).

        Arguments:
            relation_field (django.db.models.fields.related): related
                field instance.
        """
        return relation_field.related_model.objects.filter(
            **{'{}__in'.format(relation_field.field.name): [self]})

    def delete(self, using=None, keep_parents=False):
        from django.db import router
        from django.db.models import signals
        using = using or router.db_for_write(self.__class__, instance=self)

        assert self._get_pk_val() is not None, \
            "%s object can't be deleted because its %s attribute " \
            "is set to None." % (self._meta.object_name, self._meta.pk.attname)

        if self._deleted_at:
            # short-circuit here to prevent lots of nesting
            return

        # Start delete, send the pre-delete signal.
        signals.pre_delete.send(
            sender=self.__class__, instance=self, using=using)

        collector = cascade_archive(self, using, keep_parents)
        resp = collector.delete()
        # End delete, send the post-delete signal
        signals.post_delete.send(
            sender=self.__class__, instance=self, using=using)

        return resp

    delete.alters_data = True

    def really_delete(self, using=None):
        """
        Actually deletes the instance.
        """
        super(SoftDeleteMixin, self).delete(using=using)

    def to_dict(self, fields=None, exclude=None):
        """
           Return a dict containing the data in ``instance`` suitable for passing as
           a Form's ``initial`` keyword argument.

           ``fields`` is an optional list of field names. If provided, return only the
           named.

           ``exclude`` is an optional list of field names. If provided, exclude the
           named from the returned dict, even if they are listed in the ``fields``
           argument. `_deleted_at` are exclude anyway
        """
        if not exclude:
            exclude = ["_deleted_at"]
        else:
            exclude.append("_deleted_at")

        return model_to_dict(self, fields, exclude)

class SoftDeleteModelAdminMixin:
    exclude = ("_deleted", "_deleted_at")