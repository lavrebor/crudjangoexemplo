from django.db import models

class Contact(models.Model):
    firstName = models.CharField("Primeiro nome", max_length=50, blank=True, null=False)
    lastName = models.CharField("Último nome", max_length=50, blank=True, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Criado em", auto_now_add=True)


    def __str__(self):
        return self.firstName

    