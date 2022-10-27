from django.db import models
from django.contrib.auth.models import User

class Position(models.Model):
    name = models.CharField("Должность", max_length=100, primary_key=True, unique=True)
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.name

class Employer(models.Model):
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    position = models.ForeignKey(Position, verbose_name="Должность", blank=True, null=True, on_delete=models.SET_NULL)
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
    
    def __str__(self):
        return  "{0} {1} \"{2}\"".format(self.user.first_name, self.user.last_name, self.user)

