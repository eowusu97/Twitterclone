# Generated by Django 4.0.4 on 2022-04-25 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likecount',
            field=models.IntegerField(blank=True, default=0, verbose_name='like_count'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, default='anonymus', max_length=14, verbose_name='Name'),
        ),
    ]