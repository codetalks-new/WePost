import os

import pytest

from wepost.apps.auth.models import WepostUser
from wepost.apps.posts.models import Node


### 用户 pytest fixtures

@pytest.fixture()
def ut1(db):
    return WepostUser.objects.filter(username="test1").first()


@pytest.fixture()
def ut2(db):
    return WepostUser.objects.filter(username="test2").first()


@pytest.fixture()
def ut3(db):
    return WepostUser.objects.filter(username="test3").first()


@pytest.fixture()
def ut4(db):
    return WepostUser.objects.filter(username="test4").first()


@pytest.fixture()
def ut5(db):
    return WepostUser.objects.filter(username="test5").first()


@pytest.fixture()
def ut6(db):
    return WepostUser.objects.filter(username="test6").first()


### 节点 pytest fixtures
@pytest.fixture()
def node_py():
    return Node.objects.filter(code="python").first()


@pytest.fixture()
def node_flask():
    return Node.objects.filter(code="flask").first()


@pytest.fixture()
def node_js():
    return Node.objects.filter(code="javascript").first()


@pytest.fixture()
def node_vue(db):
    return Node.objects.filter(code="vue").first()


@pytest.fixture()
def node_c(db):
    return Node.objects.filter(code="c").first()
