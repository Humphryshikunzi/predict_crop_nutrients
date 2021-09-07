from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):

        return {'hello': 'world', 'more_data':{'name':'humphry', 'reg_no':'E021-01-0686/2017'}}

class HelloWorldMore(Resource):
    def get(self):

        return {'hello': 'world', 'more_data':{'name':'humphry', 'reg_no':'E021-01-0686/2017'}}        

api.add_resource(HelloWorldMore, '/')

if __name__ == '__main__':
    app.run(debug=True)