# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DieselSchemaMigrations(models.Model):
    version = models.CharField(primary_key=True, max_length=50)
    run_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = '__diesel_schema_migrations'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Prompts(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField()
    prompt_token = models.IntegerField()
    completion_token = models.IntegerField()
    prompt_text = models.CharField()
    completion_text = models.CharField()
    total_token = models.IntegerField()
    total_cost = models.FloatField()
    instruction = models.CharField()
    prompt_type = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prompts'


class Students(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    student_id = models.CharField()
    student_email = models.CharField(blank=True, null=True)
    student_card_img_url = models.CharField(blank=True, null=True)
    institution_level = models.CharField()
    institution_name = models.CharField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    free_discount_end_at = models.DateTimeField()
    half_discount_end_at = models.DateTimeField()
    student_application_valid = models.BooleanField()
    student_application_invalid_reason = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'


class Subscriptions(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    topup = models.ForeignKey('Topups', models.DO_NOTHING)
    created_at = models.DateTimeField()
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    duration_type = models.CharField()
    paid = models.BooleanField()
    is_paylater = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'subscriptions'


class Topups(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField()
    topup_amount = models.FloatField()
    paid = models.BooleanField()
    topup_type = models.CharField()

    class Meta:
        managed = False
        db_table = 'topups'


class Users(models.Model):
    id = models.UUIDField(primary_key=True)
    fullname = models.CharField()
    email = models.CharField()
    password = models.CharField()
    phone_number = models.CharField(blank=True, null=True)
    balance = models.FloatField()

    class Meta:
        managed = False
        db_table = 'users'
