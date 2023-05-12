from django.db import models
# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=250)
    year = models.IntegerField()
    image = models.ImageField(upload_to='media')
    discription = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name', 'year')
        verbose_name_plural = "movie"
