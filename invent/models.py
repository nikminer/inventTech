from django.db import models

from human_resource.models import *

# Таблица «Производители»
class Manufacture(models.Model):
    # Объявление текстового поля "Производитель"
    name = models.CharField("Производитель", max_length=100, primary_key=True, unique=True)

    # Мета класс Django отвечающий за определение различных аттрибутов
    class Meta:
        # Аттрибут отвечающий за представление записи из таблицы в единичном числе
        verbose_name = "Производитель"
        # Аттрибут отвечающий за представление записи из таблицы в множественном числе
        verbose_name_plural = "Производители"
    
    # Перегрузка метода отвечающего за строковое представление объекта 
    def __str__(self):
        return self.name
# Таблица «Тип техники»
class TechType(models.Model):
    name = models.CharField("Тип оборудования", max_length=100, primary_key=True, unique=True)
    inventCode = models.CharField("Инвентаризационный префикс", default="00", max_length=20)
   
    # Мета класс Django отвечающий за определение различных аттрибутов
    class Meta:
        # Аттрибут отвечающий за представление записи из таблицы в единичном числе
        verbose_name = "Тип оборудования"
        # Аттрибут отвечающий за представление записи из таблицы в множественном числе
        verbose_name_plural = "Типы оборудования"
    
    # Перегрузка метода отвечающего за строковое представление объекта 
    def __str__(self):
        return self.name

# Таблица "Модель техники"
class TechModel(models.Model):
    # Объявление текстового поля
    name = models.CharField("Модель", max_length=100, primary_key=True, unique=True)
    # Объявление внешнего ключа ссылающего на запись в таблице "Производители"
    manufacture = models.ForeignKey(Manufacture, verbose_name="Производитель", on_delete=models.CASCADE)
    # Объявление внешнего ключа ссылающего на запись в таблице "Тип техники"
    modeltype = models.ForeignKey(TechType, verbose_name="Тип устройства", on_delete=models.DO_NOTHING)

    # Мета класс Django отвечающий за определение различных аттрибутов
    class Meta:
        # Аттрибут отвечающий за представление записи из таблицы в единичном числе
        verbose_name = "Оборудование"
        # Аттрибут отвечающий за представление записи из таблицы в множественном числе
        verbose_name_plural = "Оборудование"
    # Перегрузка метода отвечающего за строковое представление объекта 
    def __str__(self):
        return "{0} {1} {2}".format(self.modeltype, self.manufacture, self.name)

# Таблица «Журнал техники»
class Tech(models.Model):
    inventNumber = models.CharField("Инвентаризационный номер", primary_key=True, max_length=100)
    serialNumber = models.CharField("Серийный номер", max_length=100,)
    
    # Объявление внешнего ключа ссылающего на запись в таблице "Модель техники"
    modelTech = models.ForeignKey(TechModel,  verbose_name="Модель устройства", null=True, on_delete=models.DO_NOTHING)
    # Объявление внешнего ключа ссылающего на запись в таблице "Сотрудники"
    employer = models.ForeignKey(Employer, verbose_name="Ответсвенный сотрудник", blank=True, null=True, on_delete=models.SET_NULL)

    # Мета класс Django отвечающий за определение различных аттрибутов
    class Meta:
        # Аттрибут отвечающий за представление записи из таблицы в единичном числе
        verbose_name = "Журнал Оборудования"
        # Аттрибут отвечающий за представление записи из таблицы в множественном числе
        verbose_name_plural = "Журнал Оборудования"

    # Перегрузка метода отвечающего за строковое представление объекта 
    def __str__(self):
        return self.inventNumber

