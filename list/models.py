from django.db import models
# Create your models here.
class Rent(models.Model):
    client_name=models.CharField(max_length=100)
    item=models.CharField(max_length=100)
    queantity=models.IntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    tel_number=models.CharField(max_length=100)
    creted_at=models.DateTimeField(auto_now_add=True)
    return_date=models.DateField()

    def __str__(self):
        return self.client_name