# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_address'),
        ('books', '0003_auto_20180606_0751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('comment_content', models.TextField(verbose_name='评论内容')),
                ('disabled', models.BooleanField(verbose_name='是否删除', default=False)),
                ('add_time', models.DateTimeField(verbose_name='评论时间', default=datetime.datetime.now)),
                ('comment_book', models.ForeignKey(verbose_name='评论书籍', to='books.Books')),
                ('comment_man', models.ForeignKey(verbose_name='评论用户', to='users.Passport')),
            ],
            options={
                'db_table': 's_comment_table',
            },
        ),
    ]
