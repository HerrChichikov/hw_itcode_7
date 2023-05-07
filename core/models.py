from django.db import models


class School(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"School: {self.name}"


class User(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    course = models.ManyToManyField(Course)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"Account - {self.user}"