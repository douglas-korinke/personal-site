from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to="projects/", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class LinkTarget(models.TextChoices):
    BLANK = "BL", "_blank"
    SELF = "SL", "_self"
    PARENT = "PA", "_parent"
    TOP = "TP", "_top"


class Menu(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    target = models.CharField(
        max_length=2, choices=LinkTarget.choices, default=LinkTarget.BLANK
    )

    def __str__(self):
        return self.title
