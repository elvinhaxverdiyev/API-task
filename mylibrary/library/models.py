from django.db import models
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(max_length=3000, default="Description not provided.")
    published_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
        
    
