from django.db import models

# Create your models here.

class User(models.Model):
	userId = models.AutoField
	user_name = models.CharField(max_length=300)
	user_email = models.EmailField(max_length=150)
	user_password = models.CharField(max_length=15)
	user_dob = models.DateField()

	
