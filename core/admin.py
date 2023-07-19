from django.contrib import admin

from core import models


@admin.register(models.User)
class User(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(models.School)
class School(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(models.Home)
class Home(admin.ModelAdmin):
    search_fields = ('name', 'street', 'city')


@admin.register(models.Course)
class Course(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(models.Account)
class Account(admin.ModelAdmin):
    search_fields = ('login',)
