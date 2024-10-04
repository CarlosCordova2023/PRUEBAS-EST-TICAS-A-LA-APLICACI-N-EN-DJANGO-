from django.contrib import admin
from .models import Fabricante, Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'f_vencimiento', 'fabricante')


class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    search_fields = ('nombre', 'pais')

admin.site.register(Fabricante, FabricanteAdmin)


admin.site.register(Producto, ProductoAdmin)


