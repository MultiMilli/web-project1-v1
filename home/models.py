from django.db import models

class Users(models.Model):
    name = models.CharField('Ім\'я', max_length=50)
    # email = models.CharField('Почта', max_length=150)

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name

