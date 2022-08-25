def show_all_view(data: list):
    print('In our db we have %i users. Here they are:' % len(data))
    for item in data:
        print(item.name())


def welcome():
    print("Welcome to our person mvc program")


def start_view():
    print('MVC - the simplest example')
    print('Does the data in the database exist [y/n]?')


def create_people():
    print('In this section you can enter new people. Just follow the instructions!')


def delete_id():
    print('Type the ID to be deleted')


def update():
    print('Type the ID to update')


def empty_view():
    print("Not exist data")


def end_view():
    print('Goodbye!')


