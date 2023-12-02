from django.db import models

# Create your models here.
class Sample(models.Model):
    question=models.CharField(max_length=250)
    answer = models.CharField(max_length=250)


    def __str__(self):
            return self.question