import time
import datetime
import re
import io
from django.http import JsonResponse
from django.utils.crypto import get_random_string
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
from qiniu import Auth, put_file, etag
from PIL import Image


def current_timestamp(ms=False):
    """
    :return:
    """
    if ms:
        return int(time.time() * 1000)
    return int(time.time())


def current_time(fmt='%Y-%m-%d %H:%M:%S'):
    return time.strftime(fmt, time.localtime())


def turn_time_to_timestamp(timestr, fmt='%Y-%m-%d %H:%M:%S'):
    return int(time.mktime(datetime.datetime.strptime(timestr, fmt).timetuple()))


def json_response(is_succ=False, data=None, message=None):
    """
    格式化输出
    :param is_succ:
    :param data:
    :param message:
    :return:
    """
    ret_dict = {
        'is_succ': is_succ
    }
    if data:
        ret_dict['data'] = data
    if message:
        ret_dict['message'] = message
    return JsonResponse(ret_dict)


def make_uuid(length=8, allowed_chars='0123456789', uuid_type='int'):
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


def upload_img(user_id, file):
    """
    上传图片到七牛云
    :param user_id:
    :param file:
    :return:
    """
    img = file.read()
    image = Image.open(io.BytesIO(img))

    # 构建七牛云
    q = Auth('4bialw-hER4uq285jLKC3fWnhjOhxvJo0SCjoErj', 'AyyguseqclyHe0gkFfZoslMTzAqAsX_DZNcbyZNr')
    bucket_name = 'sanford00'
    key = '{0}-{1}.{2}'.format(user_id, current_time(fmt='%Y%m%d%H%M%S'), image.format.lower())

    file_path = './image/avatar/{0}'.format(key)
    image = image.resize((400, 400), Image.ANTIALIAS)
    image.save(file_path)

    token = q.upload_token(bucket_name, key, 3600)
    ret, info = put_file(token, key, file_path, version='v2')
    img_url = 'http://r434tg1gi.hn-bkt.clouddn.com/{}'.format(key)

    assert ret['key'] == key
    assert ret['hash'] == etag(file_path)
    return img_url


if __name__ == '__main__':
    pass
    # upload_img(2, 2)
