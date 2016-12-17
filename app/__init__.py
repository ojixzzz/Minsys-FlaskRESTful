from flask import Flask

app = Flask(__name__ , static_url_path='/static')
app.config.from_object('config')

# Import a module / component using its blueprint handler variable
from app.mod_apisv1.routes import mod_apisv1

# Register blueprint(s)
app.register_blueprint(mod_apisv1)