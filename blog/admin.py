from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

class Categoria_add_admin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

class Post_add_admin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

admin.site.register(Categoria, Categoria_add_admin)
admin.site.register(Post, Post_add_admin)