from django.db import models

# Create your models here.
class college(models.Model):
    collegeId = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    strength = models.IntegerField()
    website = models.URLField()

class Principale(models.Model):
    CollegId = models.OneToOneField(
        college,
        on_delete = models.CASCADE
    )
    Qualification = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
