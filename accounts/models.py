from django.db import models


class Order(models.Model):
    phone = models.CharField(max_length=7)
    AREA = (
        ('Male', 'Male'),
        ('Hulhumale', 'Hulhumale')
    )

    house = models.CharField(max_length=100)
    road = models.CharField(max_length=100, null=True)
    landmarks = models.CharField(max_length=100, blank=True, default=None)
    additional_requests = models.CharField(max_length=500, blank=True, default=None)
    area = models.CharField(max_length=200, null=True, choices=AREA)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    STATUS = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered')
    )

    status = models.CharField(max_length=200, choices=STATUS)
    product = models.TextField(max_length=200, blank=False)
    total_price = models.DecimalField(decimal_places=2, max_digits=20, default=None)





