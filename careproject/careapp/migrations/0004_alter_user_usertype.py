# Generated by Django 4.2 on 2023-04-19 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0003_alter_user_d_o_b'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.IntegerField(null=True),
        ),
    ]
