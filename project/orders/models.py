from django.db import models


class Order(models.Model):
    class Status(models.TextChoices):
        NEW = "new"
        PROCESSING = "processing"
        SHIPPED = "shipped"
        CANCEL = "cancel"

    class Marketplace(models.TextChoices):
        AMAZON = "amazon"
        CDISCOUNT = "cdiscount"

    order_id = models.CharField(max_length=20)
    order_status = models.CharField(choices=Status.choices, max_length=20, null=True)
    order_purchase_date = models.DateField(null=True)
    order_amount = models.FloatField()
    order_shipping = models.FloatField()
    marketplace = models.CharField(choices=Marketplace.choices, max_length=20)

    def __str__(self):
        return f"{self.order_id}"
