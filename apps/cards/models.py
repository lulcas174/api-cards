from django.db import models

class Card(models.Model):
    number = models.CharField(max_length=19, unique=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'