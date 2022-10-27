from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.contrib import admin
from sequences import get_next_value
from invent.models import *
from invent.availableFilter import AvailableTechFilter


@admin.register(Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'show_tech']
    search_fields = ("name__startswith",)

    @admin.display(empty_value='0', description="Количество")
    def show_tech(self, obj):
        count = Tech.objects.filter(modelTech__manufacture__name=obj).count()
        url = (
            reverse("admin:invent_tech_changelist")
            + "?"
            + urlencode({"modelTech__manufacture__name": f"{obj.name}"})
        )
        return format_html('<a href="{0}">{1}</a>', url, count)
    pass

@admin.register(TechType)
class TechTypeAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'show_tech']
    search_fields = ("name__startswith",)

    @admin.display(empty_value='0', description="Количество")
    def show_tech(self, obj):
        count = Tech.objects.filter(modelTech__modeltype__name=obj).count()
        url = (
            reverse("admin:invent_tech_changelist")
            + "?"
            + urlencode({"modelTech__modeltype__name": f"{obj.name}"})
        )
        return format_html('<a href="{0}">{1}</a>', url, count)
    pass

@admin.register(TechModel)
class TechModelAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = [ 'name', 'manufacture', 'modeltype', 'show_tech']
    list_filter = ('modeltype__name', 'manufacture__name', )
    search_fields = ("name__startswith", "manufacture__name__startswith", "modeltype__name__startswith")

    @admin.display(empty_value='0', description="Количество")
    def show_tech(self, obj):
        count = Tech.objects.filter(modelTech=obj).count()
        url = (
            reverse("admin:invent_tech_changelist")
            + "?"
            + urlencode({"modelTech__name": f"{obj.name}"})
        )
        return format_html('<a href="{0}">{1}</a>', url, count)
    pass

@admin.register(Tech)
class TechAdmin(admin.ModelAdmin):
    empty_value_display = 'Свободно'
    fields = ['modelTech', 'serialNumber', 'employer']
    ordering = ("inventNumber", )
    list_display = ['inventNumber', 'modelTech', 'serialNumber', 'employer']
    list_filter = ('modelTech__modeltype__name', 'modelTech__manufacture__name', 'employer__position__name', AvailableTechFilter)
    search_fields = ("modelTech__name__startswith", "modelTech__manufacture__name__startswith", "modelTech__modeltype__name__startswith")
    
    def save_model(self, request, obj, form, change):
        if len(obj.inventNumber) == 0:
            obj.inventNumber = "{0}_{1:0>15}".format(
                    obj.modelTech.modeltype.inventCode, 
                    get_next_value(obj.modelTech.modeltype.name)
                )
        super().save_model(request, obj, form, change)    
    pass
