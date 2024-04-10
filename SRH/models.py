from django.db import models

class StudentDatabase(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)
    email = models.CharField(max_length=100)  # Example max_length, adjust as needed
    age = models.IntegerField()
    gender = models.CharField(max_length=10)  # Example max_length, adjust as needed

    def __str__(self):
        return self.name
