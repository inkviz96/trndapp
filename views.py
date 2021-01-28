import tornado.web
import random
from database_setup import ActivateCodes
from sqlalchemy.orm import sessionmaker
from database_setup import engine
import secrets


class CodeGeneration(tornado.web.RequestHandler):
    async def get(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        accesscode = secrets.token_urlsafe(24)
        newaccesscodein = ActivateCodes(code=accesscode, user_id='name')
        session.add(newaccesscodein)
        session.commit()
        #query = session.query(ActivateCodes.code)
        #print(query.all())
        self.render('code.html', predict=None, items=newaccesscodein)
