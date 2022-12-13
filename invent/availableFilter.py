from django.contrib.admin import SimpleListFilter

class AvailableTechFilter(SimpleListFilter):
    title = "Стутус оборудования"
    parameter_name = 'employer'
   
    def lookups(self, request, model_admin):
        return (
            ('available', 'Совободные'),
            ('unavailable', 'Занятые')
        )
    
    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().lower() == 'available':
            return queryset.filter(employer_id__isnull=True)
        elif self.value().lower() == 'unavailable':
            return queryset.filter(employer_id__isnull=False)