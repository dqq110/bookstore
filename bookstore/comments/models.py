from django.db import models
from db.base_moder import BaseModel
from users.models import Passport
from books.models import Books
from datetime import datetime
# Create your models here.

class Comments(BaseModel):
    comment_man = models.ForeignKey('users.Passport',verbose_name='用户id')
    comment_book = models.ForeignKey('books.Books',verbose_name='书籍id')
    comment_content = models.TextField(verbose_name='评论内容')
    disabled = models.BooleanField(default=False,verbose_name='是否删除')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='评论时间')

    class Meta:
        db_table = 's_comment_table'
