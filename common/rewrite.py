"""
重写一些方法
"""
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from apps.user.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import BaseAuthentication, TokenAuthentication


class SanfordModelBackend(ModelBackend):
    """
    登录验证
    """

    def authenticate(self, uuid=None, password=None, **kwargs):
        """
        原方法的 username 登录改为 uuid 登录
        :param uuid:
        :param password:
        :param kwargs:
        :return:
        """
        if uuid and password:
            try:
                user = User.objects.get(uuid=uuid)
            except ObjectDoesNotExist:
                user = None
            if user and user.check_password(password):
                return user


class SanfordTokenAuthentication(TokenAuthentication):
    """
    Token验证
    """

    def authenticate_credentials(self, key):
        """
        取消原方法的 is_active 校验, 增加Token有效期
        :param key:
        :return:
        """

        try:
            token = Token.objects.select_related('user').get(key=key)
        except ObjectDoesNotExist:
            raise exceptions.AuthenticationFailed('Not Login, Invalid token.')
        return (token.user, token)
