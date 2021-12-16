from django.db import models

from django.db import models
class TranslatorItem(models.Model):
    content = models.TextField()
    language = models.TextField(default=' ')
    translated_data = models.TextField(default=' ')
