from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from tinymce.models import HTMLField
import string  # for string constants
import random  # for generating random strings
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(editable=False, unique=True, blank=True, null=True)
    body = HTMLField()
    featured_content = models.CharField(max_length=250)
    create_date = models.DateField(auto_now_add=True)
    image =models.ImageField(null=True, blank=True, upload_to='images/')
    

    def __str__(self):
        return self.title + ' | ' + str(self.authors)  
    
    def get_absolute_url(self):
        return reverse('articleview', args=(str(self.id)))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
