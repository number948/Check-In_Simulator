from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=9)
    email = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'name: {self.name}\nphone: {self.phone}\nemail: {self.email}'
