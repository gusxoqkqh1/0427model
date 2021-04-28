from django.db import models

class User(models.Model):
    email      = models.EmailField(max_length=100, unique=True)
    password   = models.CharField(max_length=100)
    name       = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)

class Meta:
    db_table = 'users'
