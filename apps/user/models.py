from django.db import models


class User(models.Model):
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
    email_status = models.IntegerField()
    real_status = models.IntegerField()
    register_timestamp = models.BigIntegerField(blank=True, null=True)
    real_timestamp = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user'
