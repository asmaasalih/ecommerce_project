from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.

CATEGORY_CHOICES = (
	('sets','sets'),
	('half sets','half sets'),
	('nechlace','nechlace'),
	('rings','rings'),
	('earrings','earrigs'),
	('bracelets','bracelets')
)

class Category(models.Model):
	
	name   = models.CharField(max_length=200,db_index=True)
	slug   = models.SlugField(max_length=200,db_index=True,unique=True)
	parent = models.ForeignKey('self',blank=True, null=True ,related_name='children',on_delete=models.CASCADE)

	class Meta:
		unique_together = ('slug', 'parent',)  
		ordering = ('name',)
		verbose_name = "Category"
		verbose_name_plural = "Categorys"

	def __str__(self):                           
		full_path = [self.name]                 
		k = self.parent                          

		while k is not None:
			full_path.append(k.name)
			k = k.parent
		return ' -> '.join(full_path[::-1])

	def get_absolute_url(self):
		return reverse('shop:product_list_category',args=[self.slug])	

	

class Product(models.Model):
	category 	= models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
	Choices     = models.CharField(choices=CATEGORY_CHOICES, max_length=9,default='sets')
	name 		= models.CharField(max_length=200,db_index=True)
	slug 		= models.SlugField(max_length=200,db_index=True)
	Image 		= models.ImageField()
	weight      = models.FloatField(default=True)
	caliber     = models.PositiveIntegerField(default=True)
	description = models.TextField(blank=True)
	price 		= models.DecimalField(max_digits=10,decimal_places=2)
	stock 		= models.PositiveIntegerField()
	tax         = models.FloatField(default=True)
	available 	= models.BooleanField(default=True)
	created 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)
	

	class Meta:
		ordering = ('-created',)
		index_together = (('id','slug'))
		verbose_name = "Product"
		verbose_name_plural = "Products"

	def __str__(self):
		return self.name


	def get_cat_list(self):           
		k = self.category
		breadcrumb = ["dummy"]
		while k is not None:
			breadcrumb.append(k.slug)
			k = k.parent

		for i in range(len(breadcrumb)-1):
			breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
		return breadcrumb[-1:0:-1]		

	def get_absolute_url(self):
		return reverse('shop:product_detail',args=[self.id,self.slug])