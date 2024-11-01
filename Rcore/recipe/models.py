from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    receipe_name = models.CharField(max_length=255,default="Unnamed Receipe")
    receipe_description = models.TextField()
    receipe_img = models.ImageField(upload_to="receipe")
    receipe_view_count = models.PositiveIntegerField(default = 1)