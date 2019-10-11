from django.db import models
        
class House(models.Model):
    id = models.PositiveIntegerField(primary_key = true, unique = true)
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    estimate = models.ForeignKey(Estimate, on_delete=models.CASCADE)
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __init__(self, *args, **kwargs):
        super(House, self).__init__(*args, **kwargs)
        
    def __str__(self):
        return '%s, %s, %s, %s, %s' % (self.id, self.description, self.price, self.estimates, self.tax, self.location)

    def getDescription(self):
        context = {
            "area_unit": self.description.area_unit,
            "bathrooms": self.description.bathrooms,
            "bedrooms": self.description.bedrooms,
            "home_size": self.description.home_size,
            "home_type": self.description.home_type,
            "link": self.description.link,
            "property_size": self.description.property_size,
            "year_built": self.description.year_built
        }
        return context

    def getPrice(self):
        context = {
            last_sold_date: self.price.last_sold_date,
            last_sold_price: self.price.last_sold_price,
            price: self.price.price,
            rent_price: self.price.rent_price
        }
        return context

    def getEstimate(self):
        context = {
            "rentzestimate_amount": self.estimate.rentzestimate_amount,
            "rentzestimate_last_updated": self.estimate.rentzestimate_last_updated,
            "zestimate_amount": self.estimate.zestimate_amount,
            "zesimtate_last_updated": self.estimate.zestimate_last_updated
        }
        return context

    def getTax(self):
        context = {
            "tax_value": self.tax.tax_value,
            "tax_year": self.tax.tax_year
        }
        return context

    def getLocation(self):
        context = {
            "address": self.location.address,
            "city": self.location.city,
            "state": self.location.state,
            "zipcode": self.location.zipcode
        }
        return context


class Description(models.Model):
    area_unit = models.CharField(max_length=10, default="SqFt")
    bathrooms = models.DecimalField(blank = True)
    bedrooms = models.PositiveIntegerField()
    home_size = models.PositiveIntegerField(blank = True)
    home_type = models.CharField()
    link = models.URLField(unique=true)
    property_size = models.PositiveIntegerField()
    year_built = models.PositiveIntegerField()

    def __str__(self):
            return '%s, %s, %s, %s, %s, %s, %s, %s' % (self.area_unit, self.bathrooms, self.bedrooms, self.home_size, self.home_type, self.link, self.property_size, self.year_built)

class Price(models.Model):
    last_sold_date = models.DateField()
    last_sold_price = models.IntegerField()
    price = models.CharField(max_length=50)
    rent_price = models.DecimalField(blank=True)

    def __str__(self):
        return '%s, %s, %s, %s' % (self.last_sold_date, self.last_sold_price, self.price, self.rent_price)

class Estimate(models.Model):
    rentzestimate_amount = models.IntegerField()
    rentzestimate_last_updated = models.DateField()
    zestimate_amount = models.IntegerField(blank = True)
    zestimate_last_updated = models.DateField()

    def __str__(self):
            return '%s, %s, %s, %s' % (self.rentzestimate_amount, self.rentzestimate_last_updated, self.zestimate_amount, self.zestimate_last_updated)

class Tax(models.Model):
    tax_value = models.IntegerField()
    tax_year = models.PositiveIntegerField()

    def __str__(self):
            return '%s, %s' % (self.tax_value, self.tax_year)

class Location(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.PositiveIntegerField()

    def __str__(self):
            return '%s, %s, %s, %s' % (self.address, self.city, self.state, self.zipcode)