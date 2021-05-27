from flask import Flask, request
from flask_marshmallow import Marshmallow
from flask_restplus import Api, Resource, fields
from authlib.integrations.flask_client import OAuth


from settings import *
from models import *
from ma import *


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS


api = Api(app, version='1.0', title='ProjectTwo API',
          description='ProjectTwo API Boilerplate')


@api.route('/api/home')
class dinnerResource(Resource):
    def get(self):
        '''
        Home Page
        '''

        return 'home Page!!'


if __name__ == '__main__':
    app.run(debug=True)
