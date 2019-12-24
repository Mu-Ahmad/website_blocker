def Add_Url():
    with open('URL.txt', 'a') as File1:
        web_address = input('Enter complete URL: \n')
        File1.write(web_address + '\n')


def Remove_Url():
    with open('URL.txt', 'r+') as File1:
        to_remove = input('Enter complete URL: ')
        content = File1.readlines()
        File1.seek(0)
        for line in content:
            if not (to_remove in line):
                File1.write(line)
        File1.truncate()


def Edit_hours():
    print('Please us 24 hours format:')
    with open('Hours.txt', 'w') as File1:
        start = input('Enter starting hour: ')
        end = input('Enter ending hour:')
        File1.write(start + '\n' + end)


def View_list():
    with open('URL.txt', 'r') as File1:
        content = File1.readlines()
        print(content)


def main():
    chk = input('Press A to enter a new url.\nPress B to remove url.\nPress H to change working hours\nPress V to view the list of blocked urls\nPress any other button to exit.')
    chk = chk.lower()
    if chk == 'a':
        Add_Url()
    elif chk == 'b':
        Remove_Url()
    elif chk == 'h':
        Edit_hours()
    elif chk == 'v':
        View_list()
    chk1 = input('Press A for further configuration or Press B to exit')
    chk1 = chk1.lower()
    if chk1 == 'a':
        main()


main()
