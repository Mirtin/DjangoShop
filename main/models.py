from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg

# Create your models here.


class CategoryTable(models.Model):
    category = models.CharField('category', max_length=50)

    def __str__(self):
        return str(self.category)


class ProductTable(models.Model):
    price = models.DecimalField('price-$', validators=[MinValueValidator(10)], decimal_places=2, max_digits=7)
    discount = models.IntegerField('discount-%')
    name = models.CharField('name', max_length=50)
    description = models.TextField('description', max_length=500)
    cat_id = models.ForeignKey(CategoryTable, on_delete=models.CASCADE)

    def average_rating(self) -> float:
        return RatingTable.objects.filter(prod_id=self).aggregate(Avg("rating"))['rating__avg'] or 0

    def calc_price(self):
        calculated_price = self.price-self.price/100*self.discount
        return calculated_price

    def __str__(self):
        return str(self.name)


class RatingTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField('rating', validators=[MaxValueValidator(5), MinValueValidator(1)], null=False)
    prod_id = models.ForeignKey(ProductTable, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)
