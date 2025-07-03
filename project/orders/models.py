from django.db import models


class Order(models.Model):
    """
    Model for orders.

    Attributes
    ----------
    order_id : str
    order_purchase_date : date
    order_amount : float
    order_shipping : float
    order_status : "new" | "processing" | "shipped" | "cancel"
    marketplace : "amazon" | "cdiscount"
    """

    class Status(models.TextChoices):
        NEW = "new"
        PROCESSING = "processing"
        SHIPPED = "shipped"
        CANCEL = "cancel"

    class Marketplace(models.TextChoices):
        AMAZON = "amazon"
        CDISCOUNT = "cdiscount"

    order_id = models.CharField(max_length=20)
    order_purchase_date = models.DateField(null=True)
    order_amount = models.FloatField()
    order_shipping = models.FloatField()
    order_status = models.CharField(choices=Status.choices, max_length=20, null=True)
    marketplace = models.CharField(choices=Marketplace.choices, max_length=20)

    def __str__(self):
        return f"{self.order_id}"
