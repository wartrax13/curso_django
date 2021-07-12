# Generated by Django 3.2.5 on 2021-07-12 14:20

from django.db import migrations, models
import django.utils.timezone
import pypro.base.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), # noqa
                ('password', models.CharField(max_length=128, verbose_name='password')), # noqa
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')), # noqa
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all ' # noqa
                                                                              'permissions without explicitly ' # noqa
                                                                              'assigning them.', # noqa
                                                     verbose_name='superuser status')), # noqa
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')), # noqa
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')), # noqa
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into ' # noqa
                                                                          'this admin site.', verbose_name='staff ' # noqa
                                                                                                           'status')), # noqa
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be ' # noqa
                                                                          'treated as active. Unselect this instead ' # noqa
                                                                          'of deleting accounts.', # noqa
                                                  verbose_name='active')), # noqa
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')), # noqa
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will ' # noqa
                                                                        'get all permissions granted to each of their ' # noqa
                                                                        'groups.', related_name='user_set', # noqa
                                                  related_query_name='user', to='auth.Group', verbose_name='groups')), # noqa
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', # noqa
                                                            related_name='user_set', related_query_name='user', # noqa
                                                            to='auth.Permission', verbose_name='user ' # noqa
                                                                                               'permissions')), # noqa
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', pypro.base.models.UserManager()),
            ],
        ),
    ]
