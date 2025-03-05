from django.db import models

class Cars(models.Model):

    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    launch_date = models.DateField()
    image = models.ImageField(default='default.jpg', upload_to='cars_images')
    price = models.DecimalField(max_digits=100, decimal_places=2)
