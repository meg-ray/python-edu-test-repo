# Generated by Django 3.1.6 on 2021-05-20 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resources', '0010_auto_20210516_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfilePopulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('underrepresented', models.BooleanField(default=False)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceAudience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceLanguages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceUseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SignupChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='underrep',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='python_related',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='resource_type',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='url1',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='url2',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='url3',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='url_description1',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='url_description2',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='url_description3',
        ),
        migrations.AddField(
            model_name='author',
            name='biography',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='resource',
            name='audience',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='devices',
        ),
        migrations.AlterField(
            model_name='resource',
            name='submitter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='resource',
            name='use_type',
        ),
        migrations.CreateModel(
            name='ResourceURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('description', models.TextField()),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='url_resource', to='resources.resource')),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='languages',
            field=models.ManyToManyField(help_text='Choose the languages that your resource focuses on.', limit_choices_to={'active': True}, to='resources.ResourceLanguages'),
        ),
        migrations.AddField(
            model_name='resource',
            name='resource_types',
            field=models.ManyToManyField(help_text='Select all that apply.', limit_choices_to={'active': True}, to='resources.ResourceType'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='populations',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resources.profilepopulation'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='roles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resources.profilerole'),
        ),
        migrations.AddField(
            model_name='resource',
            name='audience',
            field=models.ManyToManyField(help_text="Select 'not specific' for resources for any or all audiences.", limit_choices_to={'active': True}, to='resources.ResourceAudience'),
        ),
        migrations.AddField(
            model_name='resource',
            name='devices',
            field=models.ManyToManyField(help_text='Which devices are compatible with this resource', limit_choices_to={'active': True}, to='resources.Device'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='requires_signup',
            field=models.ForeignKey(help_text='Are users required to create an account or provide their email address to access this resource?', on_delete=django.db.models.deletion.PROTECT, to='resources.signupchoice'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resources.resourcestatus'),
        ),
        migrations.AddField(
            model_name='resource',
            name='use_type',
            field=models.ManyToManyField(help_text='Select the use type that best describes this resource.', limit_choices_to={'active': True}, to='resources.ResourceUseType'),
        ),
    ]
