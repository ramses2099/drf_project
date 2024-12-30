import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    pass

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    @property
    def in_stock(self):
        return self.stock > 0
    
    def __str__(self) -> str:
        return self.name
    
class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'pending', 
        COMPLETED = 'completed'
        CANCELLED = 'cancelled'

    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,
                               choices=StatusChoices.choices,
                               default=StatusChoices.PENDING)
    
    products = models.ManyToManyField(Product, through="OrderItem", related_name="orders")

    def __str__(self) -> str:
        return f"Order {self.order_id} by {self.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


    @property
    def item_subtotal(self):
        return self.quantity * self.product.price
    
    def __str__(self) -> str:
        return f"{self.quantity} x {self.product.name} in Order {self.order.order_id}"