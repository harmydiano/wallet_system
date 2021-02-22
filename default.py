from flask_restful import Resource, Api


class Home(Resource):
    def get(self):
        return 'Welcome to Flask Rest API Setup!'
