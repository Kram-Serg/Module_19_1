from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(News)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size', 'cost') # Фильтрация
    list_display = ('title', 'cost', 'size') # Поля для отображения в списке
    search_fields = ('title',) # Поля для поиска
    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age')  # Фильтрация
    list_display = ('name', 'balance', 'age')  # Поля для отображения в списке
    search_fields = ('name',)  # Поля для поиска
    list_per_page = 30
    readonly_fields = ('balance',)