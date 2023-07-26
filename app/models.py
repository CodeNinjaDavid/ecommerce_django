from django.db import models

# Create your models here.

CATEGORY_CHOICES =(
    ('MK', 'Milk'),
    ('BM', 'Buttermilk'),
    ('FM', 'Freshmilk'),
    ('MS', 'Milkshake'),
    ('GH', 'Ghee'),
    ('YG', 'Yorghutplain'),
    ('CH', 'Cheese'),
    ('IC', 'Ice-cream'),
    
)
class product(models.Model):
    title = models.CharField(max_length=50)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    
    def __str__(self):
        return self.title
    