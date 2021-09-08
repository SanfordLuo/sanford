import time
import re
from django.http import JsonResponse
from django.utils.crypto import get_random_string
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist


def get_current_timestamp():
    """
    当前毫秒级时间戳
    :return:
    """
    return int(time.time() * 1000)


def json_response(is_succ=False, data=None, total=None, message=None):
    """
    格式化输出
    :param is_succ:
    :param data:
    :param total:
    :param message:
    :return:
    """
    ret_dict = {
        'is_succ': is_succ
    }
    if data:
        ret_dict['data'] = data
    if total:
        ret_dict['total'] = total
    if message:
        ret_dict['message'] = message
    return JsonResponse(ret_dict)


def make_uuid(length=9, allowed_chars='0123456789', uuid_type='int'):
    """
    生成uuid
    :param length:
    :param allowed_chars:
    :param uuid_type:
    :return:
    """
    success = False
    uuid = '0'
    rpt = 0
    while not success and rpt < 50:
        uuid = get_random_string(length=length, allowed_chars=allowed_chars)
        if uuid[0] != 0:
            success = True
        rpt += 1
    if uuid_type == 'int':
        return int(uuid)
    else:
        return uuid


def valid_email(email):
    """
    校验邮箱格式
    :param email:
    :return:
    """
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def valid_phone(phone):
    """
    校验手机号格式
    :param phone:
    :return:
    """
    ret = re.match(r'^1[345678]\d{9}$', phone)
    if ret:
        return True
    else:
        return False


def valid_password(password):
    """
    校验密码格式,长度>=8,必须包含一位数字,必须包含一位字母,只能包含数字和字母
    :param password:
    :return:
    """
    if len(password) < 8:
        return False
    if not any(_.isdigit() for _ in password):
        return False
    if not any(_.isalpha() for _ in password):
        return False
    if not password.isalnum():
        return False
    return True


def current_user(request):
    """
    通过token获取当前用户id
    :return:
    """
    user_id = None
    token_info = request.META.get('HTTP_AUTHORIZATION')
    if token_info:
        token = token_info.split()[1]
        try:
            user_id = Token.objects.get(key=token).user_id
        except ObjectDoesNotExist:
            user_id = None
    return user_id


if __name__ == '__main__':
    print(valid_phone("17839194009"))
