from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class yameteKudasai(Resource):

    def getgghg(self):
        return "cheater"

api.add_resource(HelloWorld, '/')
api.add_resource(yameteKudasai, '/hi')

if __name__ == '__main__':
    app.run(debug=True)
