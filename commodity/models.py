from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User

class Singer(models.Model):
    CATEGORY = (
        ('Male Group', 'Male Group'),
        ('Female Group', 'Female Group'),
        ('Male SOLO', 'Male SOLO'),
        ('Female SOLO', 'Female SOLO'),
    )

    category = models.CharField(max_length=100, choices=CATEGORY)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Commodity(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    date = models.DateField()
    content = models.TextField(max_length=500)
    image = models.FileField()
    iframe = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    album = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    time_long = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Music(models.Model):
    name = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, default="")
    music_files = models.FileField()

    def __str__(self):
        return self.name

class Order(models.Model):
    PAYMENT = (
        ('貨到付款', '貨到付款'),
        ('銀行轉帳', '銀行轉帳'),
        ('信用卡支付', '信用卡支付'),
    )
    STATUS = (
        ('備貨中', '備貨中'),
        ('運貨中', '運貨中'),
        ('當天送達', '當天送達'),
    )
    PROGRESS = (
        ('未付款', '未付款'),
        ('已付款', '已付款'),
        ('交易完成', '交易完成'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    product = models.ForeignKey(Commodity, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=100)
    phone = PhoneField(blank=True, help_text='Contact Phone Number')
    address = models.CharField(max_length=100)
    pay = models.CharField(max_length=100, choices=PAYMENT)
    status = models.CharField(max_length=100, choices=STATUS, default="備貨中")
    progress = models.CharField(max_length=100, choices=PROGRESS, default="未付款")
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.name