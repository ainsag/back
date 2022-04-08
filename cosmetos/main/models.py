from django.db import models


# # Create your models here.
# class ProductTypes(models.Model):
#     name = models.CharField(max_length=50, help_text="Name of the product type.")
#
#     def __str__(self):
#         return self.name


class Products(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_details = models.TextField()
    product_image = models.ImageField()
    # product_type = models.ForeignKey(ProductTypes, on_delete=models.PROTECT, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'Product - {self.product_name}'
