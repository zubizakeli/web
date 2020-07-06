from django.db import models
from tinymce.models import HTMLField

class Person(models.Model):   # 用户
    name = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=256)
    mail = models.CharField(max_length=32, null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    icon = models.ImageField(upload_to='icons/%Y/%m', null=True, default='icons/2020/03/default.jpg')

class Article(models.Model):  # 博客文章
    title = models.CharField(max_length=16)
    content = HTMLField()
    add_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Person, null=True)

class ArticleComment(models.Model):  # 博客评论
    content = models.CharField(max_length=100)
    article = models.ForeignKey(Article)
    owner = models.ForeignKey(Person)
    add_time = models.DateTimeField(auto_now_add=True, null=True)

class LikeArticle(models.Model):   # 博客-点赞/推荐
    article_id = models.IntegerField()
    fan_id = models.IntegerField()

class MarkArticle(models.Model):   # 博客-收藏
    article_id = models.IntegerField()
    fan_id = models.IntegerField()

class Likes(models.Model):  # 维护关注/粉丝关系
    star_id = models.IntegerField()
    fan_id = models.IntegerField()

class Discussion(models.Model):  # 论坛帖子
    title = models.CharField(max_length=32)
    content = HTMLField()
    owner = models.ForeignKey(Person)
    add_time = models.DateTimeField(auto_now_add=True, null=True)

class DiscussionResponse(models.Model):   # 帖子回复
    discussion = models.ForeignKey(Discussion)
    content = HTMLField()
    owner = models.ForeignKey(Person)
    add_time = models.DateTimeField(auto_now_add=True)

class LikeDiscussionResponse(models.Model):
    comment_id = models.IntegerField()
    fan_id = models.IntegerField()
    add_time = models.DateTimeField(auto_now_add=True)


class LikeDiscussion(models.Model):   # 帖子-点赞/推荐
    discussion_id = models.IntegerField()
    fan_id = models.IntegerField()

class MarkDiscussion(models.Model):   # 帖子-收藏
    discussion_id = models.IntegerField()
    fan_id = models.IntegerField()

