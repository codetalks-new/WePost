# coding: utf-8
import pytest

from wepost.apps.posts.services import UserNodeService

__author__ = '代码会说话'


def test_toggle_star_node(ut1, node_c, node_py, node_js):
  service1 = UserNodeService(ut1)
  nodes = [node_c, node_js, node_py]
  for node in nodes:
    assert not service1.has_star(node)
    assert not service1.has_block(node)

  for node in nodes:
    service1.star_node(node)
    assert service1.has_star(node)
    assert not service1.has_block(node)
    service1.unstar_node(node)
    assert not service1.has_star(node)
    assert not service1.has_block(node)

  for node in nodes:
    service1.block_node(node)
    assert service1.has_block(node)
    assert not service1.has_star(node)
    service1.unblock_node(node)
    assert not service1.has_star(node)
    assert not service1.has_block(node)


def test_query_nodes(ut1, node_c, node_py, node_js, node_flask, node_vue):
  service = UserNodeService(ut1)
  nodes = [node_c, node_js, node_py, node_flask]
  for node in nodes:
    service.star_node(node)
  service.block_node(node_vue)

  ret_nodes1 = list(service.query_star_nodes())
  assert len(ret_nodes1) == len(nodes)
  ret_nodes1.reverse()
  assert ret_nodes1 == nodes

  ret_nodes2 = service.query_star_nodes(keyword="py")
  assert list(ret_nodes2) == [node_py]

  blocked_nodes = list(service.query_blocked_nodes())
  assert blocked_nodes == [node_vue]
