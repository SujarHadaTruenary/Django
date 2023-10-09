from django.db import models

# Create your models here.


class todo(models.Model):
    name = models.CharField(max_length=40)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.text
