# coding: utf-8
from wepost.apps.sns.services import UserRelationService

__author__ = '代码会说话'


def test_toggle_follow_user(ut1, ut2, ut3, ut4, ut5, ut6):
  service = UserRelationService(ut1)
  users = [ut2, ut3, ut4, ut5, ut6]
  for user in users:
    assert not service.has_follow(user)
    assert not service.has_block(user)

  for user in users:
    service.follow(user)
    assert service.has_follow(user)
    assert not service.has_block(user)

    service.unfollow(user)
    assert not service.has_follow(user)
    assert not service.has_block(user)

  for user in users:
    service.block(user)
    assert service.has_block(user)
    assert not service.has_follow(user)

    service.unblock(user)
    assert not service.has_follow(user)
    assert not service.has_block(user)


def test_query_followed_or_blocked(ut1, ut2, ut3, ut4, ut5, ut6):
  service = UserRelationService(ut1)
  users = [ut2, ut3, ut4, ut5]
  for user in users:
    service.follow(user)

  ret_users1 = list(service.query_followed_users())
  assert len(ret_users1) == len(users)
  ret_users1.reverse()
  assert ret_users1 == users

  ret_users2 = list(service.query_followed_users(keyword="test3"))
  assert ret_users2 == [ut3]

  service.block(ut6)
  blocked_users = list(service.query_blocked_users())
  assert blocked_users == [ut6]
