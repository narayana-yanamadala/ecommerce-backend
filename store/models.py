from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    productName  = models.CharField(max_length=200)
    category     = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price        = models.DecimalField(max_digits=10, decimal_places=2)
    imgUrl       = models.URLField(max_length=500, help_text="Paste any image URL (Unsplash, Amazon, etc.)")
    shortDesc    = models.CharField(max_length=300, blank=True)
    description  = models.TextField(blank=True)
    avgRating    = models.DecimalField(max_digits=3, decimal_places=1, default=4.0)
    inStock      = models.BooleanField(default=True)
    discount     = models.IntegerField(default=0, help_text="Discount % (0 = no discount)")
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.productName

    class Meta:
        ordering = ['-created_at']
