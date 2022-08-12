from ... import db
from datetime import datetime

class User(db.Model):
   __tablename__ = "users"
   id = db.Column('id', db.BigInteger, primary_key = True, )
   name = db.Column('name',db.Text()) 
   created_at = db.Column('created_at',db.DateTime(), nullable=True, default=datetime.now())
   updated_at = db.Column('updated_at',db.DateTime(), nullable=True,  default=datetime.now())


def __init__(self, id, name, created_at, updated_at):
   self.id = id
   self.name = name
   self.created_at = created_at
   self.updated_at = updated_at



