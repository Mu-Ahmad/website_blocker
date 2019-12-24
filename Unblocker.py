
hosts_temp = 'hosts'
hosts_path = 'C:\Windows\System32\drivers\etc\hosts'

with open('URL.txt', 'r') as file1:
    url = file1.read()
    website_list = url.splitlines()


with open(hosts_path, 'r+') as file:
    content = file.readlines()
    file.seek(0)
    for line in content:
        if not any(website in line for website in website_list):
            file.write(line)
        file.truncate()


# print('You have Unblocked the following sites:\n%s' % url)
