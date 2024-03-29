import logging
from django.contrib import auth
from django.views.generic import View
from apps.user.models import User
from common import utils
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes
from common.rewrite import SanfordModelBackend, SanfordTokenAuthentication

logger = logging.getLogger('django')


# /user/register
class UserRegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        """
        注册用户
        :param request:
        :return:
        """
        req_data = request.data

        uuid = utils.make_uuid()
        username = req_data.get('username')
        password = req_data.get('password')
        phone = req_data.get('phone')

        if not uuid:
            return utils.json_response(message='账户生成失败,请重试')
        if not phone:
            return utils.json_response(message='请输入手机号')
        if not password:
            return utils.json_response(message='请输入密码')
        if not utils.valid_phone(phone):
            return utils.json_response(message='请输入正确格式的手机号')
        if not utils.valid_password(password):
            return utils.json_response(message='密码长度至少为8,必须包含数字字母,且只能包含数字字母,请输入正确格式的密码')

        if User.objects.filter(phone=phone):
            return utils.json_response(message='手机号已使用')
        if username and User.objects.filter(username=username):
            return utils.json_response(message='用户名重复')

        data = {
            'uuid': uuid,
            'username': username,
            'password': make_password(password, 'password'),
            'phone': phone,
            'register_timestamp': utils.current_timestamp(ms=True),
        }

        try:
            create_user = User.objects.create(**data)
            return utils.json_response(is_succ=True, data={'uuid': create_user.uuid}, message='恭喜你注册成功')
        except Exception:
            return utils.json_response(message='注册失败,请稍后重试')


# /user/login
class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        """
        登录
        :param request:
        :return:
        """
        req_data = request.data
        uuid = req_data.get('uuid')
        password = req_data.get('password')

        user = SanfordModelBackend.authenticate(request, uuid=uuid, password=password)
        if user is None:
            return utils.json_response(message='用户名或密码错误')
        try:
            token_info = Token.objects.get(user_id=user.id)
        except ObjectDoesNotExist:
            token_info = Token.objects.create(user=user)
        token = token_info.key
        username = user.username if user.username else user.uuid
        return utils.json_response(is_succ=True, data={'token': token, 'username': username})


# /user/logout
class UserLogoutAPIView(APIView):
    # authentication_classes = [SanfordTokenAuthentication]

    def get(self, request):
        """
        退出登录
        :param request:
        :return:
        """
        is_succ = True
        message = None

        token_info = request.META.get('HTTP_AUTHORIZATION')
        if token_info:
            token = token_info.split()[1]
            try:
                Token.objects.get(key=token).delete()
            except ObjectDoesNotExist:
                is_succ = False
                message = '退出登录失败'
        return utils.json_response(is_succ=is_succ, message=message)


# /user/center
class UserCenterAPIView(APIView):

    def get(self, request):
        """
        用户的详细信息
        :param request:
        :return:
        """
        user_id = utils.current_user(request)

        try:
            user_info = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return utils.json_response(message='用户不存在')

        data = {
            'user_id': user_info.id,
            'uuid': user_info.uuid,
            'username': user_info.username,
            'avatar': user_info.avatar,
            'phone': user_info.phone,
            'email': user_info.email,
            'province': user_info.province,
            'city': user_info.city,
            'email_status': user_info.email_status,
            'real_status': user_info.real_status,
            'register_timestamp': user_info.register_timestamp,
            'real_timestamp': user_info.real_timestamp
        }
        return utils.json_response(is_succ=True, data=data)

    def put(self, request):
        """
        修改用户信息
        :param request:
        :return:
        """
        user_id = utils.current_user(request)
        req_data = request.data

        try:
            user_info = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return utils.json_response(message='用户不存在')

        put_type = req_data.get('put_type')
        if put_type == 'basic':
            return self.update_basic(user_id, req_data)
        elif put_type == 'password':
            return self.update_password(user_info, req_data)
        elif put_type == 'phone':
            return self.update_phone(user_info, req_data)
        elif put_type == 'email':
            return self.update_email(user_info, req_data)
        elif put_type == 'email_status':
            return self.update_email_status(user_info, req_data)
        elif put_type == 'id_card':
            return self.update_id_card(user_info, req_data)
        elif put_type == 'avatar':
            return self.update_avatar(user_id, user_info, request.FILES.get('file'))
        else:
            return utils.json_response(message='修改用户信息类型无效')

    def delete(self, request):
        """
        注销用户
        :param request:
        :return:
        """
        user_id = utils.current_user(request)

        try:
            User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return utils.json_response(message='用户不存在')

        try:
            User.objects.filter(id=user_id).delete()
            return utils.json_response(is_succ=True, message='注销账户成功')
        except Exception:
            return utils.json_response(message='注销账户失败')

    @staticmethod
    def update_basic(user_id, req_data):
        """
        修改用户基本信息
        :param user_id:
        :param req_data:
        :return:
        """
        data = {}
        username = req_data.get('username')
        province = req_data.get('province')
        city = req_data.get('city')
        if username:
            if User.objects.filter(username=username):
                return utils.json_response(message='用户名重复')
            data['username'] = username
        if province:
            data['province'] = province
        if city:
            data['city'] = city

        if data:
            try:
                User.objects.filter(id=user_id).update(**data)
                return utils.json_response(is_succ=True, message='修改用户基本信息成功')
            except Exception:
                return utils.json_response(message='修改用户基本信息失败')
        return utils.json_response(is_succ=True, message='没有修改项')

    @staticmethod
    def update_password(user_info, req_data):
        """
        修改密码
        :param user_info:
        :param req_data:
        :return:
        """
        data = {}
        old_password = req_data.get('oldPassword')
        password = req_data.get('password')

        if not old_password:
            return utils.json_response(message='请输入旧密码')
        if not password:
            return utils.json_response(message='请输入新密码')

        if user_info.password != make_password(old_password, 'password'):
            return utils.json_response(message='旧密码不正确 重新输入')

        if not utils.valid_password(password):
            return utils.json_response(message='密码长度至少为8,必须包含数字字母,且只能包含数字字母,请输入正确格式的密码')
        data['password'] = make_password(password, 'password')

        try:
            User.objects.filter(id=user_info.id).update(**data)
            return utils.json_response(is_succ=True, message='修改密码成功')
        except Exception:
            return utils.json_response(message='修改密码失败')

    @staticmethod
    def update_phone(user_info, req_data):
        """
        修改手机号
        :param user_info:
        :param req_data:
        :return:
        """
        data = {}
        old_phone = req_data.get('oldPhone')
        phone = req_data.get('phone')

        if not old_phone:
            return utils.json_response(message='请输入旧手机号')
        if not phone:
            return utils.json_response(message='请输入新手机号')

        if user_info.phone != old_phone:
            return utils.json_response(message='旧手机号不正确 重新输入')

        if not utils.valid_phone(phone):
            return utils.json_response(message='请输入正确格式的手机号')
        if User.objects.filter(phone=phone):
            return utils.json_response(message='手机号已使用')
        data['phone'] = phone

        try:
            User.objects.filter(id=user_info.id).update(**data)
            return utils.json_response(is_succ=True, message='修改手机号成功')
        except Exception:
            return utils.json_response(message='修改手机号失败')

    @staticmethod
    def update_email(user_info, req_data):
        """
        修改邮箱
        :param user_info:
        :param req_data:
        :return:
        """
        data = {}
        old_email = req_data.get('oldEmail', '')
        email = req_data.get('email')

        if not email:
            return utils.json_response(message='请输入新邮箱')

        if old_email and user_info.email != old_email:
            return utils.json_response(message='旧邮箱不正确 重新输入')

        if not utils.valid_email(email):
            return utils.json_response(message='请输入正确格式的邮箱')
        if User.objects.filter(email=email):
            return utils.json_response(message='邮箱已使用')
        data['email'] = email

        try:
            User.objects.filter(id=user_info.id).update(**data)
            return utils.json_response(is_succ=True, message='修改/添加 邮箱成功')
        except Exception:
            return utils.json_response(message='修改/添加 邮箱失败')

    @staticmethod
    def update_email_status(user_info, req_data):
        """
        激活邮箱
        :param user_info:
        :param req_data:
        :return:
        """
        if not user_info.email:
            return utils.json_response(message='未绑定邮箱')
        if user_info.email_status:
            return utils.json_response(message='邮箱已激活')

        data = {'email_status': 1}
        try:
            User.objects.filter(id=user_info.id).update(**data)
            return utils.json_response(is_succ=True, message='激活邮箱成功')
        except Exception:
            return utils.json_response(message='激活邮箱失败')

    @staticmethod
    def update_id_card(user_info, req_data):
        """
        实名认证
        :param user_info:
        :param req_data:
        :return:
        """
        if user_info.id_card and user_info.real_status:
            return utils.json_response(message='已实名认证')

        data = {}
        id_card = req_data.get('idCard')
        if not id_card:
            return utils.json_response(message='请输入身份证')

        id_card = make_password(id_card, 'id_card')
        if User.objects.filter(id_card=id_card):
            return utils.json_response(message='身份证已使用')
        data['id_card'] = id_card
        data['real_status'] = 1
        data['real_timestamp'] = utils.current_timestamp(ms=True)

        try:
            User.objects.filter(id=user_info.id).update(**data)
            return utils.json_response(is_succ=True, message='实名认证成功')
        except Exception:
            return utils.json_response(message='实名认证失败')

    @staticmethod
    def update_avatar(user_id, user_info, file):
        """
        修改用户头像
        :param user_id:
        :param user_info:
        :param file:
        :return:
        """
        if user_info.avatar:
            last_time = user_info.avatar.split('-')[-1].split('.')[0]
            now_timestamp = utils.current_timestamp()
            if utils.turn_time_to_timestamp(last_time, fmt='%Y%m%d%H%M%S') + 60 * 60 * 2 > now_timestamp:
                return utils.json_response(message='请两小时后再次进行修改')

        data = {'avatar': utils.upload_img(user_id, file)}
        try:
            User.objects.filter(id=user_id).update(**data)
            return utils.json_response(is_succ=True, message='修改头像成功')
        except Exception:
            return utils.json_response(message='修改头像失败')
