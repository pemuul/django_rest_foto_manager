from django.db import models

# Create your models here.
class Foto(models.Model):
    id = models.AutoField(primary_key=True)
    geo = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    people_name_in_foto = models.CharField(max_length=250)
    foto_im = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} | {self.description}'
