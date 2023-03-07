from flask_restful import Resource, Api

class Home(Resource):
    def get(self):
        return {'hello': 'world'}

class About(Resource):
    def get(self):
        return {"data_num": ['About Page',"123",1]}

class Contact_us(Resource):
    def get(self):
        return {"Contact": "us"}
