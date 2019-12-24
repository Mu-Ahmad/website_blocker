
with open('URL.txt', 'r') as file1:
    url = file1.read()
    website_list = url.splitlines()

hosts_temp = 'hosts'
hosts_path = 'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'

with open(hosts_path, 'r+') as file:
    content = file.read()
    for website in website_list:
        if website in content:
            pass
        else:
            file.write(redirect + " " + website + "\n")

# print(website_list)
# print(content)
