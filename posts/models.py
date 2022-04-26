from email.mime import image
from django import db
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Post(models.Model):
    class Meta(object):
        db_table = 'post'
    name = models.CharField('Name', blank=False, max_length=14, db_index=True, default='anonymus')
    body = models.CharField('Body', blank=True, max_length=140, db_index=True)

    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )
    likecount=models.IntegerField(
        'like_count',default=0,blank=True
    )
    image= CloudinaryField(
        'image',blank=True,db_index=True
    )
