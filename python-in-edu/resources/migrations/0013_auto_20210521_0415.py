# Generated by Django 3.1.6 on 2021-05-21 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0012_auto_20210520_2251'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ResourceLanguages',
            new_name='ResourceLanguage',
        ),
        migrations.AlterField(
            model_name='resource',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='resources.resourcestatus'),
        ),
    ]