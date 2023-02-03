from django.db import models
from uuid import uuid4

class Albums(models.Model):
    id_album = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    artist =  models.CharField(max_length=255)
    release_year = models.IntegerField()
    info = models.TextField(blank=True, max_length=500)
    created_at = models.DateField(auto_now_add=True)
    
    
    