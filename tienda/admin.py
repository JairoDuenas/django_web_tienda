from django.contrib import admin
from .models import CategoriaProducto, Producto

# Register your models here.

class Categoria_add_admin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

class Producto_add_admin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  list_display = ('nombre')

admin.site.register(CategoriaProducto, Categoria_add_admin)
admin.site.register(Producto, Producto_add_admin)