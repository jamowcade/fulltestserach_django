import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fulltextsearch.settings')
import django
import random
django.setup()
from myapp.models import mylogs
from faker import Faker
fk = Faker()


from faker.providers import internet
from faker.providers import date_time


for _ in range(1000):
    fake = Faker()
    fake.add_provider(internet)
   

def papulare(value):
    for i in range(value):
        name = fk.name()
        description = fk.text()
        ip_address = fake.ipv4_private()
        port = fake.port_number()
        http_response = fake.iso8601()
        obj = mylogs.objects.get_or_create(name=name,description=description,ip_address=ip_address,port=port,http_response=http_response)


def main():
    no = int(input("how many data entry you want"))
    papulare(no)

if __name__ == "__main__":  
    main()    