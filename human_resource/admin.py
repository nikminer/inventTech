from django.contrib import admin
from human_resource.models import *

# Декоратор отвечает, за регистрацию модели данных в админке
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass

# Декоратор отвечает, за регистрацию модели данных в админке
@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    # Определяем отображение пустых значений
    empty_value_display = '-empty-'
    # Указываем какие поля таблицы отображаются в общем списке
    list_display = ('user', 'user_name', 'position')
    # Указываем по каким полям доступна фильтрация
    list_filter = [ 'position__name',]
    # Указываем по каким полям таблицы производить поиск
    search_fields = ("position__name__startswith",)
    
    # Специализированный display поле собирающее разрозненные поля в ФИО.
    @admin.display(empty_value='0', description="ФИО")
    def user_name(self, obj):
        return "{0} {1}".format(obj.user.first_name, obj.user.last_name)
    pass
