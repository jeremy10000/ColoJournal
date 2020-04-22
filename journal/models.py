from django.db import models

from users.models import User


class Journal(models.Model):

    name = models.CharField(max_length=80, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    shared = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Journaux"

    def __str__(self):
        return self.name


class Page(models.Model):

    name = models.CharField(max_length=80, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
