from django.contrib import admin
from .models import Product, Component, BillOfMaterials, Inventory

class BillOfMaterialsInline(admin.TabularInline):
    model = BillOfMaterials
    extra = 1  # Permite agregar filas dinámicamente en el admin

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'created_at')
    search_fields = ('sku', 'name')
    inlines = [BillOfMaterialsInline]

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('part_number', 'name', 'category', 'safety_stock')
    list_filter = ('category',)
    search_fields = ('part_number', 'name')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('get_part_number', 'current_stock', 'in_transit_stock', 'warehouse_location')
    
    def get_part_number(self, obj):
        return obj.component.part_number
    get_part_number.short_description = 'Número de Parte'
