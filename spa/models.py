from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
Users = get_user_model()


class UserProfileRegister(models.Model):
    class Meta:
        db_table = 'user_register'

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class PostModel(models.Model):
    class Meta:
        db_table = 'post'
        verbose_name = 'Допис'
        verbose_name_plural = 'Дописи'

    topic = models.CharField(max_length=50)
    description = models.CharField(max_length=500, default='', blank=True)

    def __str__(self):
        return f"Post on by {self.topic}"


class CommentsModel(models.Model):
    class Meta:
        db_table = 'comments'
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, related_name='comments', on_delete=models.CASCADE)
    data_comments = models.DateTimeField()
    text_comments = models.CharField(max_length=500, default='', blank=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.topic}"
