from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja
# Import Ninja class from the ninja.py file

class Dojo:
    # Lining up the table with attributes of the class, data coming in will be parsed with the object
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    # Pass in the list of Dojo Locations on the Home Page (Under All Dojos)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        #Results come back as a list of dictionaries
        # d = each row / data
        dojos = []
        for d in results:
            dojos.append(cls(d))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_ninjas').query_db(query, data)
        return result

    @classmethod
    def get_ninja(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_ninjas').query_db(query, data)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(n))
        return dojo