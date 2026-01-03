from app import app
# cambia questo e decommenta per cambiare tabella da creare poi run current file
# from dbModels.table import class
from dbModels.db import db

with app.app_context():
    db.drop_all()
    db.create_all()