from flask import render_template, redirect, request
from past.builtins import raw_input
from app import app
from model import Person
import view


@app.route('/')
def index():
    # call the render template
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    # call the render template
    return render_template('person.html')


@app.route('/person_detail', methods=["POST"])
def person_detail():
    # here we take the values of the fields
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    # we enter the values to Person
    p = Person(id=id_person, first_name=first_name, last_name=last_name)
    # we create dictionary, to take the data and send to view
    data = {'id': p.id, 'name': p.first_name, 'last_name': p.last_name}
    Person.create(p)
    print(data)
    return render_template('person_detail.html', value=data)


def create_p():
    view.create_people()
    id_p = input(print("Enter person code: "))
    first_name = input(print("Type the person's name: "))
    last_name = input(print("Type the person's last name: "))
    p = Person(id=id_p, first_name=first_name, last_name=last_name)
    Person.create(p)
    people_in_db = Person.get_all()
    data = [(i.id, i.first_name, i.last_name) for i in people_in_db]
    view.show_all_view(data)


@app.route('/people')
def people():
    # Saves all the information of the person object
    people_in_db = Person.get_all()
    data = [(i.id, i.first_name, i.last_name) for i in people_in_db]
    # The data to be stored is printed
    print(data)
    # calls render template
    return render_template('people.html', value=data)


def show_all():
    # gets list of all Person objects
    people_in_db = Person.get_all()
    # calls view
    return view.show_all_view(people_in_db)


def start():
    # call the views
    view.start_view()
    # Request for information
    input = raw_input()
    # Data entry is conditioned
    if input == 'y':
        # call the function
        return show_all()
    else:
        # call the function
        return view.end_view()


@app.route('/person_update/<id_person>', methods=['GET'])
def update(id_person):
    person_db = Person.get_all()
    # we look for the id
    data = [(i.id, i.first_name, i.last_name) for i in person_db if i.id == id_person]
    # calls the render template
    return render_template('update.html', value=data)


@app.route('/person_update/<id_person>', methods=['POST'])
def update_p(id_person):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    data = {'id': id_person, 'name': first_name, 'last_name': last_name}
    Person.update(data)
    return render_template('person_detail.html', value=data)


@app.route('/person_delete/<id_person>', methods=["POST"])
def delete(id_person):
    # call the methods of class
    Person.delete(id_person)
    # The ip address is called
    return redirect('/people')


def delet():
    show_all()
    view.delete_id()
    input = raw_input()
    Person.delete(input)


def update_con():
    show_all()
    view.update()
    input = raw_input()
    people = Person.get_all()
    data = [(i.id, i.first_name, i.last_name) for i in people]
    for i in people:
        try:
            if input == data[0][0]:
                print("Write the person's name: ")
                first_name = raw_input()
                print("Type the person's last name: ")
                last_name = raw_input()
                data = {'id': input, 'name': first_name, 'last_name': last_name}
                Person.update(data)
        except ValueError:
            print("The people not exist")


if __name__ == "__main__":
    # running controller function
    start()