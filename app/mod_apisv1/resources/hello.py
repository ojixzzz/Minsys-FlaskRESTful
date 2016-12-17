import traceback, sys
from flask_restful import Resource, url_for, request
from app.mod_apisv1.common.utils import return_error

class HelloRes(Resource):
    def get (self):
        try:
            data_out = {
                'data': 'Hello World'
            }
            
            return data_out

        except Exception as e:
            print(e)
            ex_type, ex, tb = sys.exc_info()
            traceback.print_tb(tb)
            return return_error(500, 'API Error')