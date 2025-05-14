from django.contrib import admin
from apps.blog.models import Category, Post

admin.site.register(Category)
admin.site.register(Post)