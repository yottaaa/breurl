from django.db import models

# Create your models here.
class Data(models.Model):
    url = models.TextField()
    slug = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug
