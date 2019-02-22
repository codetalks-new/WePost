# coding: utf-8
from wepost.apps.auth.models import WepostUser
from wepost.apps.posts.enums import UserNodeStarState
from wepost.apps.posts.models import Node, UserNodeStar

__author__ = '代码会说话'


class UserNodeService:
  """用户与节点相关服务类"""

  def __init__(self, user: WepostUser):
    self.user = user

  def _update_star_state(self, node: Node, star_state: UserNodeStarState):
    """更新关注状态"""
    obj, created = UserNodeStar.objects.update_or_create(user=self.user, node=node, state=star_state)
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
