from django.db import migrations
from datetime import datetime
import csv

def load_initial_data(apps, schema):

    House = apps.get_model("api", "House")
    Description = apps.get_model("api", "Description")
    Price = apps.get_model("api", "Price")
    Estimate = apps.get_model("api", "Estimate")
    Tax = apps.get_model("api", "Tax")
    Location = apps.get_model("api", "Location")

    with open('challenge_data.csv') as list_data:
        reader = csv.reader(list_data)
        header = next(reader)

        houses = []

        for row in reader:
            area_unit = row[0]
            bathrooms = row[1]
            bedrooms = row[2]
            home_size = row[3]
            home_type = row[4]
            last_sold_date = datetime.strptime(row[5], "%m/%d/%Y").date()
            last_sold_price = row[6]
            link = row[7]
            price = row[8]
            property_size = row[9]
            rent_price = row[10]
            rentzestimate_amount = row[11]
            rentzestimate_last_updated = datetime.strptime(row[12], "%m/%d/%Y").date()
            tax_value = row[13]
            tax_year = row[14]
            year_built = row[15]
            zestimate_amount = row[16]
            zestimate_last_updated = datetime.strptime(row[17], "%m/%d/%Y").date()
            zillow_id = row[18]
            address = row[19]
            city = row[20]
            state = row[21]
            zipcode = row[22]

            desc = Description(area_unit=area_unit, bathrooms=bathrooms,
                            bedrooms=bedrooms, home_size=home_size,
                            home_type=home_type, link=link,
                            property_size=property_size, year_built=year_built)
                               
            price = Price(last_sold_date=last_sold_date,
                        last_sold_price=last_sold_price,
                        price=price, rent_price=rent_price)

            estimate = Estimate(rentzestimate_amount=rentzestimate_amount,
                            rentzestimate_last_updated=rentzestimate_last_updated,
                            zestimate_amount=zestimate_amount,
                            zestimate_last_updated=zestimate_last_updated)

            tax = Tax(tax_value=tax_value, tax_year=tax_year) 

            location = Location(address=address, city=city, state=state, zipcode=zipcode)

            house = House(id=zillow_id, description=desc,
                        price=price, estimate=estimate, tax=tax,
                        location=location)
            
            houses.append(house)
        Houses.objects.bulk_create(houses)


def reverse_func(app, schema):
    House = apps.get_model("api", "House")

    House.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = []
    operations = [
        migrations.RunPython(load_initial_data, reverse_func)
    ]
    