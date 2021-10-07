from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Login(Resource):
    def post(self):
        print("User added")
        print("bago")
        return {'msg': 'User added successfully'}

api.add_resource(Login, '/login')

print("this is now changed!")


if __name__ == '__main__':
    app.run(debug=True)
