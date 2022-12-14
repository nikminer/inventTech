from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.contrib import admin
from sequences import get_next_value
from invent.models import *
from invent.availableFilter import AvailableTechFilter


# Декоратор отвечает, за регистрацию модели данных в админке
@admin.register(Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    # Указываем какие поля таблицы отображаются в общем списке
    list_display = [ 'name', 'show_tech'] 
    # Указываем по каким полям таблицы производить поиск
    search_fields = ("name__startswith",) 

    # Специализированный display поле отображающий кол-во записей в журнале техники имеющих текущего производителя.
    @admin.display(empty_value='0', description="Количество")
    def show_tech(self, obj):
        # Делаем запрос к таблице "Модель техники", чтобы подсчитать сколько имеется моделей от текущего производителя
        count = Tech.objects.filter(modelTech__manufacture__name=obj).count()
        # Формируем ссылку на таблицу "Модель техники", с фильтрацией по текущему производителю
        url = (
            reverse("admin:invent_tech_changelist")
            + "?"
            + urlencode({"modelTech__manufacture__name": f"{obj.name}"})
        )
        # Формируем HTML вставку, в поле записи, чтобы отобразить кол-во и дать возможность отфильтровать по текущему производителю
        return format_html('<a href="{0}">{1}</a>', url, count)
    pass

# Декоратор отвечает, за регистрацию модели данных в админке
@admin.register(TechType)
class TechTypeAdmin(admin.ModelAdmin):
    # Указываем какие поля таблицы отображаются в общем списке
    list_display = [ 'name', 'show_tech']
    # Указываем по каким полям таблицы производить поиск
    search_fields = ("name__startswith",)

    # Специализированный display поле отображающий кол-во записей в журнале техники имеющих текущему типу.
    @admin.display(empty_value='0', description="Количество")
    def show_tech(self, obj):
        # Делаем запрос к таблице "Модель техники", чтобы подсчитать сколько имеется моделей от текущему типу
        count = Tech.objects.filter(modelTech__modeltype__name=obj).count()
        # Формируем ссылку на таблицу "Модель техники", с фильтрацией по текущему типу
        url = (
            reverse("admin:invent_tech_changelist")
            + "?"
            + urlencode({"modelTech__modeltype__name": f"{obj.name}"})
        )
        # Формируем HTML вставку, в поле записи, чтобы отобразить кол-во и дать возможность отфильтровать по текущему типу
        return format_html('<a href="{0}">{1}</a>', url, count)
    pass

# Декоратор отвечает, за регистрацию модели данных в админке
@admin.register(TechModel)
class TechModelAdmin(admin.ModelAdmin):
    # Определяем отображение пустых значений
    empty_value_display = '-empty-'
    # Указываем какие поля таблицы отображаются в общем списке
    list_display = [ 'name', 'manufacture', 'modeltype', 'show_tech']
    # Указываем по каким полям доступна фильтрация
    list_filter = ('modeltype__name', 'manufacture__name', )
    # Указываем по каким полям таблицы производить поиск
    search_fields = ("name__startswith", "manufacture__name__startswith", "modeltype__name__startswith")

    # Специализированный display поле отображающий кол-во записей в журнале техники имеющих текущей модели.
    @admin.display(empty_value='0', description="Количество")
    def show_tech(self, obj):
        # Делаем запрос к таблице "Модель техники", чтобы подсчитать сколько имеется моделей от текущей модели
        count = Tech.objects.filter(modelTech=obj).count()
        # Формируем ссылку на таблицу "Модель техники", с фильтрацией по текущей модели
        url = (
            reverse("admin:invent_tech_changelist")
            + "?"
            + urlencode({"modelTech__name": f"{obj.name}"})
        )
        # Формируем HTML вставку, в поле записи, чтобы отобразить кол-во и дать возможность отфильтровать по текущей модели
        return format_html('<a href="{0}">{1}</a>', url, count)
    pass

# Декоратор отвечает, за регистрацию модели данных в админке
@admin.register(Tech)
class TechAdmin(admin.ModelAdmin):
    # Определяем отображение пустых значений
    empty_value_display = 'Свободно'
    # Указываем какие поля таблицы доступны для редактирования
    fields = ['modelTech', 'serialNumber', 'employer']
    # Указываем в каком порядке идёт сортировка записей
    ordering = ("inventNumber", )
    # Указываем какие поля таблицы отображаются в общем списке
    list_display = ['inventNumber', 'modelTech', 'serialNumber', 'employer']
    # Указываем по каким полям доступна фильтрация
    list_filter = ('modelTech__modeltype__name', 'modelTech__manufacture__name', 'employer__position__name', AvailableTechFilter)
    # Указываем по каким полям таблицы производить поиск
    search_fields = ("modelTech__name__startswith", "modelTech__manufacture__name__startswith", "modelTech__modeltype__name__startswith")
    
    # Перегружаем Django метод ответсвенный за сохнаение записи
    def save_model(self, request, obj, form, change):
        # Если инвентаризационный номер пустой
        if len(obj.inventNumber) == 0:
            # То формируем его, получая инвентаризационный префикс из типа товара и получая новое значение номерной серии
            obj.inventNumber = "{0}_{1:0>15}".format(
                    obj.modelTech.modeltype.inventCode, 
                    get_next_value(obj.modelTech.modeltype.name)
                )
        # Сохраняем запись
        super().save_model(request, obj, form, change)    
    pass
