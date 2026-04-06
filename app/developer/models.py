from django.db import models
from accounts.models import CPPUser
from django.utils import timezone

class DatabaseFile(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1023, blank=True)
    file = models.FileField(upload_to='rag_dataset', blank=True)
    date_added = models.DateTimeField("date added", default=timezone.now)
    uploader = models.ForeignKey(CPPUser, on_delete=models.SET(None), blank=True)




# Create your models here.
