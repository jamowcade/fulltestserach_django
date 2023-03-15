import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fulltextsearch.settings')
import django
import random
django.setup()
from myapp.models import mylogs
from faker import Faker
fk = Faker()
from faker.providers import internet

for _ in range(1):
    fake = Faker()
    fake.add_provider(internet)
    fake = Faker()
def papulare(value):
    for i in range(value):
       
        sw_user = fake.first_name()
       
        sr_user = fake.first_name()
        h_ip = fake.ipv4()
        h_time = str(fake.date_time())
        http_code = [200, 201, 404, 500]
        http_time = h_time.replace("-","/")
        http_code = [200, 201, 404, 500]
        # random_http_code = random.choice(http_code)
        msg = [f"%SSH-5-SSH2_USERAUTH: User {sw_user} authentication for SSH2 Session from {h_ip} (tty = 0) using crypto cipher 'aes256-ctr', hmac 'hmac-sha1' Succeeded",
            f"pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost={h_ip} user={sr_user}",
            f"{h_ip} - - [{http_time} +0300] '{fake.http_method()} /{fake.uri_path()} HTTP/1.1' {random.choice(http_code)} {fake.port_number()}"]      
        # random_massage =random.choice(msg)




        time = http_time
        name = sr_user
        description = random.choice(msg)
        ip_address = h_ip
        obj = mylogs.objects.get_or_create(name=name,ip_address=ip_address,time=time,massage=description)


def main():
    no = int(input("how many data entry you want"))
    papulare(no)

if __name__ == "__main__":  
    main()    