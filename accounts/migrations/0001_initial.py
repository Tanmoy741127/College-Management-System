# Generated by Django 3.0.7 on 2020-10-23 19:24

import accounts.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('phoneno', models.BigIntegerField(unique=True, verbose_name='phone no')),
                ('name', models.CharField(default='No_NAME', max_length=50)),
                ('userflag', models.BooleanField(default=False)),
                ('is_topleveladmin', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('verified_by_teacher', models.BooleanField(default=False)),
                ('designation', models.TextField(default='-1', null=True)),
                ('verified', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', accounts.managers.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='answerPaper',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.UUIDField(null=True)),
                ('questionid', models.UUIDField(null=True)),
                ('answerlink', models.TextField(null=True)),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
                ('ipaddress', models.GenericIPAddressField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='marksData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.UUIDField(null=True)),
                ('questionid', models.UUIDField(null=True)),
                ('answerid', models.UUIDField(null=True)),
                ('marks', models.BigIntegerField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OTPData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneno', models.BigIntegerField()),
                ('otp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='questionPaper',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('link', models.TextField(null=True)),
                ('total_marks', models.BigIntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='registrationLinkShare',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('course', models.CharField(choices=[('fashion', 'Fashion'), ('food', 'Food'), ('grocery', 'Grocery'), ('electronics', 'Electronics'), ('handcrafts', 'Handcrafts')], max_length=50, null=True)),
                ('open', models.BooleanField(default=False)),
                ('expired', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='studentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[('fashion', 'Fashion'), ('food', 'Food'), ('grocery', 'Grocery'), ('electronics', 'Electronics'), ('handcrafts', 'Handcrafts')], max_length=50, null=True)),
                ('rollno', models.TextField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
