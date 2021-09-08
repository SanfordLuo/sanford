from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 删除不需要的原字段
    last_login = None
    is_superuser = None
    first_name = None
    last_name = None
    is_staff = None
    is_active = None
    date_joined = None

    id = models.BigAutoField(primary_key=True)
    uuid = models.BigIntegerField(unique=True)
    username = models.CharField(unique=True, max_length=255, blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(unique=True, max_length=11)
    email = models.CharField(max_length=255, blank=True, null=True)
    id_card = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    email_status = models.IntegerField(default=0)
    real_status = models.IntegerField(default=0)
    register_timestamp = models.BigIntegerField(blank=True, null=True)
    real_timestamp = models.BigIntegerField(blank=True, null=True)
    last_login_timestamp = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'
