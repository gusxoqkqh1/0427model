from django.db import models

class Category(models.Model):
    name        = models.CharField(max_length=50 ,unique=True)
    destination = models.ManyToManyField('Destination', through='Destination_Category')

    class Meta:

        db_table = 'categories'

class Destination(models.Model):
    name      = models.CharField(max_length=50 ,unique=True)
    image_url = models.CharField(max_length=3000)

    class Meta:

        db_table ='destinations'

class Destination_Category(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:

        db_table ='destination_categories'

class Product(models.Model):
    name       = models.CharField(max_length=50 ,unique=True)
    price      = models.DecimalField(max_digits=6, decimal_places=3)
    class_room = models.SmallIntegerField()
    detail     = models.CharField(max_length=1000)
    category   = models.ForeignKey(Category, on_delete=models.CASCADE)
    gu         = models.ForeignKey('Gu', on_delete=models.CASCADE) # 강남구
    city       = models.ForeignKey('City', on_delete=models.CASCADE) # 서울시
    service    = models.ManyToManyField('Service', through='Convenience_Service')
    latitude   = models.DecimalField(max_digis=15, decimal_places=15) # 위도 ?
    longitude  = models.DecimalField(max_digis=15, decimal_places=15) # 경도 ?
    is_reset   = models.BooleanField() # 리셋
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:

        db_table = 'products'

class Product_Image(models.Model):
    image_url = models. ImageField(max_length=3000)
    product   = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:

        db_table ='product_images'

class Gu(models.Model):
    name = models.CharField(max_length=50 ,unique=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE)

class Meta:

    db_table = 'gu'

class City(models.Model):
    name = models.CharField(max_length=50 ,unique=True)

    class Meta:

        db_table = 'cities'

class Service(models.Model):
    name             = models.CharField(max_length=50 ,unique=True)
    service_category = models.ForeignKey('Service_Category', on_delete=models.CASCADE)

    class Meta:

        db_table = 'services'

class Service_Category(models.Model):
    name = models.CharField(max_length=50 ,unique=True)

    class Meta:

        db_table = 'service_categories'

class Convenience_Service(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:

        db_table = 'convenience_services'
