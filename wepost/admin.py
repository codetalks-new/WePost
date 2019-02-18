# coding: utf-8
from django.conf.urls import url
from django.contrib.admin import AdminSite
from django.contrib.admin.apps import AdminConfig
from django.urls import path



class MyAdminSite(AdminSite):
    site_header = "WePost 管理后台"
    site_title = site_header
    index_title = site_title
    site_url = None # 此项目暂时没有主页
    # index_template = "admin/my_index.html"

    def get_urls(self):
        urls = super(MyAdminSite, self).get_urls()
        return urls

class MyAdminConfig(AdminConfig):
    default_site = "wepost.admin.MyAdminSite"