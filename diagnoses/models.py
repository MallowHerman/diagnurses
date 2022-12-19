from django.db import models
from django.template.defaultfilters import slugify
import uuid

class Domains(models.Model):
    name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    number = models.IntegerField(null=True)
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True) 

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Classes(models.Model):
    name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    number = models.IntegerField(null=True, blank=True)
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True) 

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Diagnoses(models.Model):
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    diagnosis = models.CharField(max_length=1000, unique=True)
    diagnosis_code = models.CharField(max_length=300, null=True, unique=True)
    slug = models.CharField(max_length=1000, null=True, blank=True, unique=True)
    definition = models.TextField(null=True)
    defining_characteristics = models.TextField(null=True, blank=True)
    related_factors = models.TextField(null=True, blank=True)
    at_risk_population = models.TextField(null=True, blank=True)
    associated_condition = models.TextField(null=True, blank=True)
    nic = models.TextField(null=True, blank=True)
    noc = models.TextField(null=True, blank=True)
    domain = models.ForeignKey(Domains, on_delete=models.SET_NULL, null=True)
    classe = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    STATUS = (
        ('Pending', 'Pending'),
        ('Approved','Approved')
    )

    accepted = models.CharField(max_length=200, null=True, choices=STATUS, default='Pending')

    def __str__(self):
        return self.diagnosis

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.diagnosis )
        return super().save(*args, **kwargs)
