from django.db import models

# Create your models here.
class regional_structure(models.Model):
    region =models.CharField(max_length=50)
    district =models.CharField(max_length=50)
    rsd_id=models.IntegerField()

    def save(self):
        return super(regional_structure, self).save()
