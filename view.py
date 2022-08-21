def show_all_view(data: list):
    print('In our db we have %i users. Here they are:' % len(data))
    for item in data:
        print(item.name())


def welcome():
    print("Welcome to our person mvc program")


def start_view():
    print('MVC - the simplest example')
    print('Do you want to see everyone in my db?[y/n]')


def create_people():
    print('In this section you can enter new people. Just follow the instructions!')


def delete_id():
    print('Type the ID to be deleted')


def end_view():
    print('Goodbye!')
