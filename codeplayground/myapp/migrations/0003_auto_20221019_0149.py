# Generated by Django 3.2.15 on 2022-10-18 17:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20221010_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_discussion',
            name='addtime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='addtime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='addtime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='addtime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='addtime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
