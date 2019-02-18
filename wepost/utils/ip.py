# coding=utf-8
from django.core.handlers.wsgi import WSGIRequest


def get_real_ip(request: WSGIRequest):
    """
    读取真实的 IP，处理有代理的情况
    对应 nginx 配置
    :
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    :param request:
    :return: ip 地址
    """
    forward_header = request.META.get("HTTP_X_FORWARD_FOR")
    ip_list = forward_header[0] if forward_header else None
    if ip_list:
        return ip_list.split(',')[0]
    real_ip = request.META.get("HTTP_X_REAL_IP")
    if real_ip:
        return real_ip
    return request.META["REMOTE_ADDR"]
