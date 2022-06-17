from django.db import models
from django.utils.html import format_html

# Create your models here.
class Category(models.Model):
    c_name = models.CharField(max_length=100)
    c_image = models.FileField(upload_to='upload', null=True, blank=True)
    c_description = models.TextField(max_length=255, null=True, blank=True)
    c_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.c_name

    def showimg_category(self):
        if self.c_image:
            return format_html('<img src="'+ self.c_image.url +'" height="50px"')
        return ''
    showimg_category.allow_tags = True

class Product(models.Model):
    p_code = models.CharField(max_length=10, unique=True)
    p_slug = models.SlugField(max_length=200, unique=True)
    p_name = models.CharField(max_length=100)
    p_description = models.TextField(max_length=255, null=True, blank=True)
    p_price = models.FloatField(default=0)
    p_image = models.ImageField(upload_to='products', null=True, blank=True)
    p_category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    p_recommend = models.BooleanField(default=False)
    p_status = models.BooleanField(default=False)
    p_created = models.DateTimeField(auto_now_add=True)
    p_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-p_created']
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.p_name

    def showimg_product(self):
        if self.p_image:
            return format_html('<img src="'+ self.p_image.url +'" height="50px"')
        return ''
    showimg_product.allow_tags = True

    def get_comment_count(self):
        return self.commentproduct_set.count()

class CommentProduct(models.Model):
    comment_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment_comment = models.CharField(max_length=100)
    comment_rating = models.IntegerField(default=0)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'CommentProduct'

    def __str__(self):
        return self.comment_comment

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images/")

    def __str__(self):
        return self.product.p_name

class Contact(models.Model):
    contactname = models.CharField(max_length=255)
    contactlastname = models.CharField(max_length=255)
    contactemail = models.EmailField()
    contactdescription = models.TextField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.contactemail