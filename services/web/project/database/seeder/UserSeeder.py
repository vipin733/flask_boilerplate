from project import db
from ..model import User

def seedDB():
    try:
        db.session.add(User(name="user 1"))
        db.session.commit()
    except:
        print("An exception occurred")
   

