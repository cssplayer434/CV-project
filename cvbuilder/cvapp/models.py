

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class CVTemplate(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    preview_image = models.ImageField(upload_to='template_previews/', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class CV(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cvs')
    title = models.CharField(max_length=150, default='My CV')
    selected_template = models.ForeignKey(CVTemplate, on_delete=models.SET_NULL, null=True, blank=True)

    # Personal fields
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=200, blank=True)
    summary = models.TextField(blank=True)
    photo = models.ImageField(upload_to="profiles/", blank=True, null=True)

    # We store complex sections as JSON (list of objects) for simplicity
    skills = models.TextField(blank=True, help_text="Comma-separated skills or use admin to add")
    # Allow NULL at the DB level so older rows without these fields won't cause IntegrityErrors
    experience = models.JSONField(default=list, blank=True, null=True)
    education = models.JSONField(default=list, blank=True, null=True)
    projects = models.JSONField(default=list, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.owner.username}"
