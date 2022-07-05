from enum import unique
from tkinter import CASCADE
from django.db import models
import uuid




UserState=[
    ('new','NEW'),
    ('Active','ACTIVE'),
    ('Blocked', 'BLOCKED'),
    ('Banned','BANNED'),
]
class webUser(models.Model):
    login_id=models.UUIDField(default=uuid.uuid4, primary_key=True, null=False)
    Password= models.CharField(max_length=20, null=False)
    State=models.CharField(max_length=100,choices=UserState)
    def __str__(self):
        return f"{self.Password} to {self.State}"

class Customer(models.Model):
    id=models.UUIDField(default=uuid.uuid4, editable=False, null=False, primary_key= True)
    address= models.CharField(max_length=50)
    Phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    web=models.OneToOneField(webUser,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id} to {self.email}"

class Account(models.Model):
    id=models.UUIDField(default=uuid.uuid4, primary_key=True)
    Billing_address=models.CharField(max_length=100, null=False)
    is_closed=models.BooleanField()
    opend=models.DateTimeField(auto_now=True)
    closed=models.DateTimeField(auto_now=True)
    cust=models.OneToOneField(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.Billing_address} to {self.closed}"
OrderStatus=[
    ('New','NEW'),
    ('Hold','HOLD'),
    ('shipped','SHIPPED'),
    ('delivered','DELIVERED'),
    ('closed','CLOSED')
]

class Order(models.Model):
    numb=models.IntegerField
    ordered=models.DateField(auto_now=True)
    shipped=models.DateField()
    sip_to=models.CharField(max_length=100)
    Status=models.CharField(max_length=50,choices=OrderStatus)
    total=models.IntegerField
    Accnt=models.ForeignKey(Account, on_delete=models.CASCADE, null= True, unique= True)

    def __str__(self):
        return f"{self.numb} to {self.total}"
class shoping_cart(models.Model):
    created_Date=models.DateTimeField(auto_now=True)
    WebUser=models.OneToOneField(webUser, on_delete=models.CASCADE, null=True)
    accnt=models.OneToOneField(Account, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return f"{self.created_Date}"

class payment(models.Model):
    id=models.UUIDField(default=uuid.uuid4, primary_key=True, null=False)
    paid_Date=models.DateTimeField(auto_now=True)
    total=models.IntegerField
    details=models.TextField
    ordr=models.ForeignKey(Order, on_delete=models.CASCADE)
    acc=models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    def __str__(self) :
        return f"{self.id} to {self.details}"




class Product(models.Model):
    id=models.UUIDField(default=uuid.uuid4, primary_key=True, null=False)
    name=models.CharField(max_length=100, null=False)
    supplier=models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.id} to {self.supplier} "


class Line_item(models.Model):
    quantit=models.IntegerField
    price= models.IntegerField
    shopingCart=models.ForeignKey(shoping_cart, on_delete=models.CASCADE, null= False)
    prodct=models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    ord=models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return f"{self.quantit} to {self.price}"