from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="media/products/")
    stock = models.PositiveIntegerField()
    is_active = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    field1 = models.FileField(upload_to="media/products/", default="asd")
    emailfield = models.EmailField(null=True,blank=True)
    field3 = models.BigIntegerField(null=True,blank=True)
    field4 = models.JSONField(null=True,blank=True)
    ip_field = models.GenericIPAddressField(null=True,blank=True)

    datefield = models.DateField(null=True,blank=True)
    datetimefield = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title