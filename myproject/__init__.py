from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from training_settings import postgresql as settings

user,password,host,port,database = settings.values()

uri = f'postgresql://{user}:{password}@{host}:{port}/{database}'
app = Flask(__name__)

app.config["SECRET_KEY"] = 'Nikita123'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

from myproject.puppies.views import puppies_blueprint
from myproject.owners.views import owners_blueprint

app.register_blueprint(owners_blueprint, url_prefix = '/owners')
app.register_blueprint(puppies_blueprint, url_prefix = '/puppies')