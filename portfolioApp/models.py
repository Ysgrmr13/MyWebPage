from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=22)
    descript = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/images/',help_text='image size : 1366x768')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title