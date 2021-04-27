from django.db import models


class Category(models.Model):
    name         = models.CharField(max_length=50)
    destination  = models.ManyToManyField('Destination', through='Destination_Category')

    class Meta:
        db_table = 'categories'

class Destination(models.Model):
    name      = models.CharField(max_length=50)
    image_url = models.CharField(max_length=3000)

    class Meta:
        db_table ='destinations'

class Destination_Category(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table ='destination_categories'

class Product(models.Model):
    name       = models.CharField(max_length=50)
    price      = models.DecimalField(max_digits=6, decimal_places=2)
    rising     = models.IntegerField()
    detail     = models.CharField(max_length=1000)
    category   = models.ForeignKey(Category, on_delete=models.CASCADE)
    gu         = models.ForeignKey('Gu', on_delete=models.CASCADE)
    city       = models.ForeignKey('City', on_delete=models.CASCADE)
    service    = models.ManyToManyField('Service', through='Convenience_Service')
    latitude   = models.DecimalField(max_digis=15, decimal_places=5) # 위도 ?
    longitude  = models.DecimalField(max_digis=15, decimal_places=5) # 경도 ?
    is_reset   = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'products'

class Product_Image(models.Model):
    image_url = models.CharField(max_length=3000)
    product   = models.ForeignKey(Product, on_delete=models.CASCADE) 
    
    class Meta:
        db_table ='product_images'

class Gu(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    class Meta:
        db_table = 'gu'


class City(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'cities'


class Service(models.Model):
    name             = models.CharField(max_length=50)
    service_category = models.ForeignKey('Service_Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'services'

class Service_Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'service_categories'

class Convenience_Service(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        db_table = 'convenience_services'

