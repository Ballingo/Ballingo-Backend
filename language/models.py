from django.db import models

class Language(models.Model): 
    language = models.CharField(
        choices=[
            ('en', 'English'), 
            ('es', 'Spanish'), 
            ('de', 'German'), 
            ('ar', 'Arabic'),
            ('ja', 'Japanese')
        ], 
        max_length=20
    )

    def __str__(self):
        return self.language

