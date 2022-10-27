from django.contrib import admin
from human_resource.models import *

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('user', 'user_name', 'position')
    list_filter = [ 'position__name',]
    search_fields = ("position__name__startswith",)
    
    @admin.display(empty_value='0', description="ФИО")
    def user_name(self, obj):
        return "{0} {1}".format(obj.user.first_name, obj.user.last_name)
    pass
