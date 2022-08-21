import json


class Person(object):

    def __init__(self, id=None, first_name=None, last_name=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    # returns Person name, ex: John Doe
    def name(self):
        return "{0} {1} {2}".format(self.id, self.first_name, self.last_name)

    @classmethod
    # returns all people inside db.txt as list of Person objects
    def get_all(cls):
        result = list()
        with open('db.json') as json_file:
            data = json.load(json_file)
            try:
                for p in data:
                    person = Person(p['id'], p['first_name'], p['last_name'])
                    result.append(person)
            except ValueError:
                print("Dont exist people")
        return result

    @classmethod
    # Returns a new person and saves it in the db.json file.
    def create(cls, p):
        new = {"id": p.id, "first_name": p.first_name, "last_name": p.last_name}
        with open('db.json', "r+", encoding="utf-8") as file:
            data = json.load(file)
            data.append(new)
            file.seek(0)
            json.dump(data, file)

    @classmethod
    # Update a people
    def update(cls, id_person):
        with open('db.json') as json_file:
            data = json.load(json_file)
            data.update()


    @classmethod
    # Removes a person from the file
    def delete(cls, id_person):
        with open('db.json') as json_file:
            data = json.load(json_file)
        try:
            result = [person for person in data if person['id'] != id_person]
            print(result)
            with open('db.json', 'w', encoding="utf-8") as file:
                file.write(json.dumps(result))
        except ValueError:
            print("The people dont exist")

