# coding: utf-8
from django.db.models import QuerySet, Q

from wepost.apps.auth.models import WepostUser
from wepost.apps.posts.enums import UserNodeStarState, UserNodeSortType
from wepost.apps.posts.models import Node, UserNodeStar
from wepost.utils.sort import SortField, SortDirection

__author__ = '代码会说话'


class UserNodeService:
  """用户与节点相关服务类"""

  def __init__(self, user: WepostUser):
    self.user = user

  def _update_star_state(self, node: Node, state: UserNodeStarState):
    """更新关注状态"""
    obj, created = UserNodeStar.objects.update_or_create(user=self.user, node=node, state=state)
    return obj, created


  def _delete_node(self, node: Node):
    """移除跟某一节点关系"""
    return UserNodeStar.objects.filter(user=self.user, node=node).delete()

  def star_node(self, node: Node):
    """关注节点"""
    return self._update_star_state(node, UserNodeStarState.FOLLOWING)

  def unstar_node(self, node: Node):
    """取消关注节点"""
    return self._delete_node(node)

  def block_node(self, node: Node):
    """屏蔽节点"""
    return self._update_star_state(node, UserNodeStarState.BLOCKING)

  def unblock_node(self, node: Node):
    """取消屏蔽节点"""
    return self._delete_node(node)

  def _check_star_state(self, node: Node, state: UserNodeStarState):
    return UserNodeStar.objects.filter(user=self.user, node=node, state=state).exists()

  def has_star(self, node: Node):
    """是否已关注"""
    return self._check_star_state(node, UserNodeStarState.FOLLOWING)

  def has_block(self, node: Node):
    """是否已屏蔽"""
    return self._check_star_state(node, UserNodeStarState.BLOCKING)

  def _query_related_nodes(self, state: UserNodeStarState, sort_type: UserNodeSortType = UserNodeSortType.CREATED,
                           keyword: str = None):
    if sort_type == UserNodeSortType.ACTIVE_DEGREE:
      sort = SortField("active_degree", SortDirection.DESC)
    elif sort_type == UserNodeSortType.UPDATED:
      sort = SortField("updated", SortDirection.DESC)
    else:
      sort = SortField("usernodestar__created", SortDirection.DESC)
    node_set = self.user.node_set
    qs = node_set.all().filter(usernodestar__state=state).order_by(sort.ordering)
    if keyword:
      qs = qs.filter(Q(name__icontains=keyword) | Q(brief__icontains=keyword))
    return qs

  def query_star_nodes(self, sort_type: UserNodeSortType = UserNodeSortType.CREATED, keyword: str = None):
    """查询已关注的节点"""
    return self._query_related_nodes(UserNodeStarState.FOLLOWING, sort_type=sort_type, keyword=keyword)

  def query_blocked_nodes(self, keyword: str = None):
    """查询已屏蔽的节点"""
    return self._query_related_nodes(UserNodeStarState.BLOCKING, keyword=keyword)
