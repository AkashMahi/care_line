# Generated by Django 4.2 on 2023-04-19 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0002_support_alter_user_cr_status_alter_user_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='d_o_b',
            field=models.DateField(null=True),
        ),
    ]