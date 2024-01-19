from django.contrib import admin
from .models import PostModel, CommentsModel

admin.site.register(PostModel)
admin.site.register(CommentsModel)
# Register your models here.
