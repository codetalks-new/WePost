# coding: utf-8
import os

from fabric import Config, Connection, task


hosts = ["ubuntu@127.0.0.1"]
APP_HOME = "/var/www/wepost-plugin/wepost/"
APP_NAME = "wepost"
pm2 = "/home/ubuntu/.yarn/bin/pm2"
pip = "/home/ubuntu/.pyenv/versions/wepost/bin/pip"
py = "/home/ubuntu/.pyenv/versions/wepost/bin/python"


@task(hosts=hosts, default=True)
def deploy(c):
    c.run("echo $PATH && echo $SHELL")
    with c.cd(APP_HOME):
        c.run("git checkout .")
        c.run("git pull")
        c.run(f"{pip} install -q -r requirements.txt")
        c.run(f"{py} manage_prod.py migrate --noinput")
        c.run(f"{py} manage_prod.py collectstatic --noinput")
        c.run(f"{pm2} restart wepost")


@task(hosts=hosts)
def unc(c):
    """更新nginx 配置"""
    # c.local("git push")
    with c.cd(APP_HOME):
        c.run("git checkout .")
        c.run("git pull")
        c.run("pwd")
        c.run("sudo cp nginx.conf /etc/nginx/")
        c.run("sudo nginx -s reload")


@task(hosts=hosts)
def cc(c):
    """更新静态资源"""
    with c.cd(APP_HOME):
        c.run("git checkout .")
        c.run("git pull")
        c.run(f"{py} manage_prod.py collectstatic --noinput")


@task(hosts=hosts)
def getdb(c):
    """把数据库下载下来"""
    with c.cd(APP_HOME):
        c.get("db.sqlite3")

@task(hosts=hosts)
def status(c):
    """ 显示应用状态 """
    c.run(f"{pm2} list")
    c.run(f"{pm2} show {APP_NAME}")

@task(hosts=hosts)
def upload(c,filepath):
    basename = os.path.basename(filepath)
    c.put(filepath, os.path.join("/tmp",basename))