from django.db import models

class Table(models.Model):
    number = models.IntegerField(unique=True)  # Уникальный номер столика
    seats = models.IntegerField()  # Количество мест
    is_available = models.BooleanField(default=True)  # Доступность столика

    def __str__(self):
        return f"Table {self.number} - {'Available' if self.is_available else 'Unavailable'}"
