from django.contrib.admin import SimpleListFilter

class AvailableTechFilter(SimpleListFilter):
    # Указывает текстовое обозначение
    title = "Статус оборудования"
    # Параметр отвечает за определение в параметрах GET зпроса 
    parameter_name = 'employer'
   
    # Перегружаем метод ответственный за отображение параметров фильтрации
    def lookups(self, request, model_admin):
        return (
            ('available', 'Свободные'),
            ('unavailable', 'Занятые')
        )
    
    # Перегружаем метод ответственный за формирование запроса фильтра
    def queryset(self, request, queryset):
        # Если не задан то возвращаем обычный запрос
        if not self.value():
            return queryset
        # Если фильтр соответствует значению "Свободные", то фильтруем по тем записям где нет сотрудника
        if self.value().lower() == 'available':
            return queryset.filter(employer_id__isnull=True)
        # Если фильтр соответствует значению "Занятые", то фильтруем по тем записям где есть сотрудник
        elif self.value().lower() == 'unavailable':
            return queryset.filter(employer_id__isnull=False)