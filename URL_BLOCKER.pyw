import time
from datetime import datetime as dt

with open('URL.txt', 'r') as file1:
    url = file1.read()
    website_list = url.splitlines()

with open('Hours.txt', 'r') as file2:
    hrs = file2.read()
    hours = hrs.splitlines()

hosts_temp = 'hosts'
hosts_path = 'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, int(hours[0])) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, int(hours[1])):
        # print("y")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        # print("L")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(60)
