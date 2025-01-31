from django.db import models

# Create your models here.
class Category(models.Model):
    category_title=models.CharField(max_length=250,null=True, blank=True)
    category_image = models.ImageField(upload_to="category/", null=True, blank=True )
    def __str__(self):
        return f"{self.category_title}"
    

    
class Item(models.Model):
    item_title = models.CharField(max_length=250,null=True, blank=True)
    item_image = models.ImageField(upload_to="item/", null=True, blank=True )
    def __str__(self):
        return f"{self.item_title}"

class Arrival(models.Model):
    arrival_title = models.CharField(max_length=250,null=True, blank=True)
    arrival_image = models.ImageField(upload_to="arrival/", null=True, blank=True )
    def __str__(self):
        return f"{self.arrival_title}"

class Product(models.Model):
    product_title = models.CharField(max_length=250,null=True, blank=True)
    product_image = models.ImageField(upload_to="product/", null=True, blank=True )
    product_price=models.DecimalField(max_digits=5,decimal_places=0,null=True, blank=True)
    product_quantity_int= models.IntegerField(null=True, blank=True)
    product_description = models.CharField(max_length=200,null=True, blank=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    product_trade = models.BooleanField(default=False)
    product_new = models.BooleanField(default=False)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    product_item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    product_arrival = models.ForeignKey(Arrival, on_delete=models.CASCADE, null=True, blank=True)
    
  

    def __str__(self):
        return f"{self.product_title}"




class Contact(models.Model):
    contact_name = models.CharField(max_length=50,null=True, blank=True)
    contact_lastname = models.CharField(max_length=50,null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_sms= models.TextField(max_length=500, null=True, blank=True)
    
    def __str__(self):
            return f"{self.contact_name} {self.contact_lastname}"