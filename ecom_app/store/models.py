from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='category/', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created',]
        verbose_name_plural = 'categories'
class Product(models.Model):
       name = models.CharField(max_length=255, blank=True, null=True)
       category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
       preview_des = models.CharField(max_length=255, verbose_name='Short Descriptions')
       description = models.TextField(max_length=255, verbose_name=' Descriptions')
       image=models.ImageField(max_length=255, blank=False, null=True)
       price = models.FloatField()
       old_price = models.FloatField(default=0.00, null=True, blank=False)
       is_stock = models.BooleanField(default=True)
       created = models.DateTimeField(auto_now_add=True)
       def __str__(self):
            return self.name
       
class ProductImage(models.Model):
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
     image = models.ImageField(upload_to='products/')
     created = models.DateTimeField(auto_now_add=True,)
     def __str__(self):
        return str(self.product.name)

