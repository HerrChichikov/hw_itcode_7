from datetime import date

from django.db import models


class Home(models.Model):
    street = models.CharField(max_length=255, blank=True)
    house = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"Home: {self.get_full_address()}"

    def get_full_address(self):
        return f"{self.city}, {self.street}, {self.house}"

    class Meta:
        verbose_name = "Адрес проживания"
        verbose_name_plural = "Адреса проживания"


class School(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"School: {self.name}"

    class Meta:
        verbose_name = "Школа"
        verbose_name_plural = "Школы"


class User(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Course(models.Model):
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    course = models.ManyToManyField(Course)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    home = models.OneToOneField(Home, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_created=True, null=True, blank=True)

    def __str__(self):
        return f"Account - {self.user}"

    class Meta:
        ordering = ["user"]
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"
