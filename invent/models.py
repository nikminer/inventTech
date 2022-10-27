from django.db import models

from human_resource.models import *

class Manufacture(models.Model):
    name = models.CharField("Производитель", max_length=100, primary_key=True, unique=True)

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"
    
    def __str__(self):
        return self.name

class TechType(models.Model):
    name = models.CharField("Тип оборудования", max_length=100, primary_key=True, unique=True)
    inventCode = models.CharField("Инвентаризационный префикс", default="00", max_length=20)
    class Meta:
        verbose_name = "Тип оборудования"
        verbose_name_plural = "Типы оборудования"

    def __str__(self):
        return self.name

class TechModel(models.Model):
    name = models.CharField("Модель", max_length=100, primary_key=True, unique=True)
    manufacture = models.ForeignKey(Manufacture, verbose_name="Производитель", on_delete=models.CASCADE)
    modeltype = models.ForeignKey(TechType, verbose_name="Тип устройства", on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"
    
    def __str__(self):
        return "{0} {1} {2}".format(self.modeltype, self.manufacture, self.name)

class Tech(models.Model):
    inventNumber = models.CharField("Инвентаризационный номер", primary_key=True, max_length=100)
    serialNumber = models.CharField("Серийный номер", max_length=100,)
    
    modelTech = models.ForeignKey(TechModel,  verbose_name="Модель устройства", null=True, on_delete=models.DO_NOTHING)
    employer = models.ForeignKey(Employer, verbose_name="Ответсвенный сотрудник", blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Журнал Оборудования"
        verbose_name_plural = "Журнал Оборудования"
    
    def __str__(self):
        return self.inventNumber

