# Generated by Django 3.1.14 on 2022-10-18 23:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0007_auto_20221018_2323'),
        ('operations', '0002_banner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': 'バナー', 'verbose_name_plural': 'バナー'},
        ),
        migrations.AlterModelOptions(
            name='coursecomments',
            options={'verbose_name': 'コースのコメント', 'verbose_name_plural': 'コースのコメント'},
        ),
        migrations.AlterModelOptions(
            name='userask',
            options={'verbose_name': '問い合わせ', 'verbose_name_plural': '問い合わせ'},
        ),
        migrations.AlterModelOptions(
            name='usercourse',
            options={'verbose_name': 'ユーザーのコース', 'verbose_name_plural': 'ユーザーのコース'},
        ),
        migrations.AlterModelOptions(
            name='userfavorite',
            options={'verbose_name': 'お気に入り', 'verbose_name_plural': 'お気に入り'},
        ),
        migrations.AlterModelOptions(
            name='usermessage',
            options={'verbose_name': 'ユーザーのメッセージ', 'verbose_name_plural': 'ユーザーのメッセージ'},
        ),
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='アップロード時間'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='banner/%Y/%m', verbose_name='バナーの画像'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='index',
            field=models.IntegerField(default=0, verbose_name='順番'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(max_length=100, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='url',
            field=models.URLField(max_length=100, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='coursecomments',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='アップロード時間'),
        ),
        migrations.AlterField(
            model_name='coursecomments',
            name='comments',
            field=models.CharField(max_length=200, verbose_name='コメントの内容'),
        ),
        migrations.AlterField(
            model_name='coursecomments',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='コース'),
        ),
        migrations.AlterField(
            model_name='coursecomments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー名'),
        ),
        migrations.AlterField(
            model_name='userask',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='アップロード時間'),
        ),
        migrations.AlterField(
            model_name='userask',
            name='course_name',
            field=models.CharField(max_length=50, verbose_name='コース名'),
        ),
        migrations.AlterField(
            model_name='userask',
            name='mobile',
            field=models.CharField(max_length=11, verbose_name='携帯番号'),
        ),
        migrations.AlterField(
            model_name='userask',
            name='name',
            field=models.CharField(max_length=20, verbose_name='ユーザー名'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='アップロード時間'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='コース'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー名'),
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='アップロード時間'),
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='fav_id',
            field=models.IntegerField(verbose_name='データID'),
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='fav_type',
            field=models.IntegerField(choices=[(1, 'コース'), (2, '教育機関'), (3, '講師')], default=1, verbose_name='お気に入りのカテゴリ'),
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー名'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='アップロード時間'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='has_read',
            field=models.BooleanField(default=False, verbose_name='既読'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='message',
            field=models.CharField(max_length=200, verbose_name='メッセージ'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー名'),
        ),
    ]
