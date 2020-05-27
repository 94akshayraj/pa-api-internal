from app.service.vec import VecService
from tornado.web import Application, RequestHandler
import tornado
import json
from bson import json_util
import time

class VecController(RequestHandler):

    def post(self):
        try:
            query=tornado.escape.json_decode(self.request.body)
            start_time = time.time()
            prediction = VecService(query).get_response()
            print('rere',prediction)
            print("--- %s seconds ---" % (time.time() - start_time))
            self.finish(json.dumps(prediction,default=json_util.default))
        except Exception as error:
            print(error)
        finally:
            return 
