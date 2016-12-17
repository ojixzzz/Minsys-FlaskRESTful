from flask import Blueprint
from flask_restful import Api, Resource, url_for
from app.mod_apisv1.resources.hello import HelloRes

mod_apisv1 = Blueprint('mod_apisv1', __name__, url_prefix='/apis/v1')
apis = Api(mod_apisv1)

apis.add_resource(HelloRes, '/hello')
