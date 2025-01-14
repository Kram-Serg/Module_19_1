from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=100, unique=True)  # имя покупателя
    balance = models.DecimalField(max_digits=100, decimal_places=2)  # баланс
    age = models.IntegerField()  # возраст

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100, null=True)  # название игры
    cost = models.DecimalField(max_digits=100, decimal_places=2)  # цена
    size = models.DecimalField(max_digits=100, decimal_places=2)  # размер файлов игры
    description = models.TextField(blank=True)  # описание
    age_limited = models.BooleanField(default=False)  # ограничение возраста 18+
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=100)  # название новости
    content = models.TextField(blank=True)  # описание новости
    date = models.DateTimeField(auto_now_add=True)  # дата выхода новости

    def __str__(self):
        return self.title


class TestTable(models.Model):
    author = models.CharField(blank=True, null=True)
    article = models.TextField(blank=True, null=True)  # This field type is a guess.
    publication_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.author