from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=255,null=True)
    image=models.ImageField(upload_to='item_images',null=True)
    class Meta:
        ordering=('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class item(models.Model):
    category=models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    price=models.FloatField()
    description=models.TextField(blank=True, null=True)
    image=models.ImageField(upload_to='item_images')
    is_sold=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'items'

    def __str__(self):
        return self.name

