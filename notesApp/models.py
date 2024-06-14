from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    tags = models.CharField(max_length=100, null=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Notes, self).save(*args, **kwargs)
    
    