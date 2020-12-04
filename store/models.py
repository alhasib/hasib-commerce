from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank = True)
    name = models.CharField(max_length = 250, null=True, blank=True)
    email = models.CharField(max_length = 250, blank=True, null=True)

    def __str__(self):
        return self.name 
    
class Product(models.Model):
    name = models.CharField(max_length = 250, blank=True, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name 

    @property
    def imgurl(self):
        try:
            url = self.image.url 
        except:
            url = ''
        return url 
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, blank = True, null = True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=True, null=True)
    transaction_id = models.CharField(max_length = 250, blank = True, null = True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        s = 0
        for orderitem in orderitems:
            s = s + orderitem.get_total
        return s 

    @property
    def get_cart_items(self):
        cart_items = self.orderitem_set.all()
        total = 0 
        for item in cart_items:
            total = total + item.quantity

        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank = True, null=True)
    order = models.ForeignKey(Order, on_delete = models.CASCADE, blank = True, null = True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total 

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE, blank = True, null = True)
    address = models.CharField(max_length = 250, null=True, blank=True)
    city = models.CharField(max_length = 250, blank=True, null=True)
    state = models.CharField(max_length = 250, blank=True, null=True)
    zipcode = models.CharField(max_length = 250, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
