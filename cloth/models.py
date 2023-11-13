from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Add Hashtag')

    def __str__(self):
        return f'#{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cost = models.PositiveIntegerField()
    tag = models.ManyToManyField(Tag, related_name='content_name')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.created_at}'


class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    total = models.IntegerField(verbose_name="Total")
    product = models.ManyToManyField(Product)
    date_and_time = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)
    address = models.CharField(verbose_name="Address", max_length=255)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
