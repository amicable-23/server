from django.db import models



# Create your models here.
class food(models.Model):
    title = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    datecreated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    qty = models.IntegerField(default=1)
    image = models.ImageField(upload_to="asset") 
