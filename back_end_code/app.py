from flask import Flask
from flask_restful import Resource, Api
from pg_app_apis import Home, About, Contact_us

app = Flask(__name__)
api = Api(app)

# class Home(Resource):
#     def get(self):
#         return {'hello': 'world'}
#
# class About(Resource):
#     def get(self):
#         return {'Welcome': 'About Page'}

api.add_resource(Home, '/')
api.add_resource(About, '/About')
api.add_resource(Contact_us, '/api/Contact_us')

if __name__ == '__main__':
    app.run(debug=True)