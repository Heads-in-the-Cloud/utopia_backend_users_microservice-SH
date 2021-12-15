#!/usr/bin/env python
# encoding: utf-8
# ######################################################################################################################
# ########################################                               ###############################################
# ########################################      Flask Initialization     ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
import os
from config import Config

from flask import Flask
from flask_migrate import Migrate

from flask_jwt_extended import jwt_required

app = Flask(__name__)
app.config.from_object(Config)

# Initializing the SQLAlchemy ORM database created in the models.py file
from models import db
db.init_app(app)

# Initializing Marshmallow serialization schemas
from schemas import *
ma.init_app(app)

# Initializing the Flask-Restful Api Builder
from resources import api
api.init_app(app)

# Initializing the Flask-Migration Handler
migrate = Migrate(db, app)


# ######################################################################################################################
# ########################################                               ###############################################
# ########################################         Make Runnable         ###############################################
# ########################################                               ###############################################
# ######################################################################################################################


if __name__ == "__main__":
    app.run(debug=True)
