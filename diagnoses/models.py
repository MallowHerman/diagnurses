from django.db import models
from django.template.defaultfilters import slugify
import uuid

class Domains(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True) 

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-")
        return super().save(*args, **kwargs)

class Classes(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True) 

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-")
        return super().save(*args, **kwargs)

class Diagnoses(models.Model):
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=1000)
    slug = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    domain = models.ForeignKey(Domains, on_delete=models.SET_NULL, null=True, blank=True)
    classe = models.ForeignKey(Classes(), on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True) 

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + "-")
        return super().save(*args, **kwargs)
