from django.db import models
from django.contrib.auth.models import User

# Таблица «Должности»
class Position(models.Model):
    # Объявление текстового поля "Должность"
    name = models.CharField("Должность", max_length=100, primary_key=True, unique=True)
    # Мета класс Django отвечающий за определение различных аттрибутов
    class Meta:
        # Аттрибут отвечающий за представление записи из таблицы в единичном числе
        verbose_name = "Должность"
        # Аттрибут отвечающий за представление записи из таблицы в множественном числе
        verbose_name_plural = "Должности"
    # Перегрузка метода отвечающего за строковое представление объекта 
    def __str__(self):
        return self.name

# Таблица «Сотрудники»
class Employer(models.Model):
    # Прямая привязка Django таблицы User к текущей, содержащей стандарные данные о пользователе
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    # Объявление внешнего ключа ссылающего на запись в таблице "Должности"
    position = models.ForeignKey(Position, verbose_name="Должность", blank=True, null=True, on_delete=models.SET_NULL)
    class Meta:
        # Аттрибут отвечающий за представление записи из таблицы в единичном числе
        verbose_name = "Сотрудник"
        # Аттрибут отвечающий за представление записи из таблицы в множественном числе
        verbose_name_plural = "Сотрудники"
    # Перегрузка метода отвечающего за строковое представление объекта 
    def __str__(self):
        return  "{0} {1} \"{2}\"".format(self.user.first_name, self.user.last_name, self.user)

