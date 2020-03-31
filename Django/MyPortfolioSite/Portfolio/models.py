from django.db import models

# Create your models here.


class Skill(models.Model):
    techId = models.AutoField(primary_key=True)
    techName = models.CharField(max_length=100)
    techStrength = models.IntegerField()

    def __str__(self):
        return self.techName
