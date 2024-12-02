from django.contrib import admin
from django.utils.html import format_html

from electronics.models import NetworkElectronics, Product


@admin.register(NetworkElectronics)
class NetworkComponent(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'country', 'city', 'link_type', 'supplier', 'duty', 'created_date', 'level',)
    list_filter = ('city',)
    search_fields = ('city',)
    date_hierarchy = 'created_date'
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(duty=0)
    clear_debt.short_description = "Очистить задолженность перед поставщиком"

    def supplier_link(self, obj):
        if obj.supplier:
            return format_html('<a href="{}">{}</a>', obj.supplier.get_absolute_url(), obj.supplier.name)
        return "Нет поставщика"

    supplier_link.short_description = 'Поставщик'
    supplier_link.admin_order_field = 'supplier__name'


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id', 'title', 'model', 'release_date',)
    list_filter = ('id', 'title', 'model', 'release_date',)
    search_fields = ('title',)
