# Generated by Django 3.2.9 on 2022-07-15 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careerguide', '0003_alter_schedule_expire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='categories',
            field=models.JSONField(verbose_name='Categories'),
        ),
    ]