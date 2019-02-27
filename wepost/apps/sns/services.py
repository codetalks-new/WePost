# coding: utf-8
from wepost.apps.auth.models import WepostUser
from wepost.apps.sns.enums import UserRelationState
from wepost.apps.sns.models import UserRelation

__author__ = '代码会说话'


class UserRelationService:
  def __init__(self, user: WepostUser):
    self.user = user

  def _update_relation(self, to: WepostUser, state: UserRelationState):
    """更新关注状态"""
    return UserRelation.objects.update_or_create(from_user=self.user, to_user=to, state=state)

  def _delete_relation(self, to: WepostUser):
    """移除对某一用户的关系"""
    return UserRelation.objects.filter(from_user=self.user, to_user=to).delete()

  def _check_relation(self, to: WepostUser, state: UserRelationState):
    return UserRelation.objects.filter(from_user=self.user, to_user=to, state=state).exists()

  def follow(self, to: WepostUser):
    return self._update_relation(to, UserRelationState.FOLLOWING)

  def unfollow(self, to: WepostUser):
    return self._delete_relation(to)

  def block(self, to: WepostUser):
    return self._update_relation(to, UserRelationState.BLOCKING)

  def unblock(self, to: WepostUser):
    return self._delete_relation(to)

  def has_follow(self, to: WepostUser):
    return self._check_relation(to, UserRelationState.FOLLOWING)

  def has_block(self, to: WepostUser):
    return self._check_relation(to, UserRelationState.BLOCKING)

  def _query_related(self, state: UserRelationState, keyword: str = None):
    user_set = self.user.followed_or_blocked.filter(userrelation_to__state=state).order_by(
      "-userrelation_to__created")
    if keyword:
      user_set = user_set.filter(username__icontains=keyword)

    return user_set

  def query_followed_users(self, keyword: str = None):
    return self._query_related(state=UserRelationState.FOLLOWING, keyword=keyword)

  def query_blocked_users(self, keyword: str = None):
    return self._query_related(state=UserRelationState.BLOCKING, keyword=keyword)
