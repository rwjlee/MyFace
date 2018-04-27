from django.db import models
from django.conf import settings

# Create your models here.

class User(models.Model):
    email = models.EmailField(null=False, unique=True)
    username = models.CharField(max_length=128, null=True)
    password = models.CharField(max_length=128, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Follow(models.Model):
    following = models.ForeignKey(User, related_name='has_followers', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name='is_followings', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('following', 'follower')

class Post(models.Model):
    user = models.ForeignKey(User, related_name='has_posts', on_delete=models.CASCADE)
    target_user = models.ForeignKey(User, related_name='got_messages', on_delete=models.CASCADE, null=True)
    content = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='has_comments', on_delete=models.CASCADE)
    content = models.TextField(null=False)
    post = models.ForeignKey(Post, related_name='has_comments', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Photo(models.Model):
    title = models.CharField(max_length=128, null=True)
    user = models.ForeignKey(User, related_name = 'has_photos', on_delete=models.CASCADE, null=True)
    img_file = models.ImageField(upload_to='media/%Y/%m')
    profile_pic = models.IntegerField(null=True)
    