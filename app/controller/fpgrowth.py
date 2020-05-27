from app.service.fpgrowth import FPGrowthService
from tornado.web import Application, RequestHandler
import tornado
import json
from bson import json_util
import time

class FPGrowthController(RequestHandler):

    def post(self):
        # query=tornado.escape.json_decode(self.request.body)
        try:
            query=tornado.escape.json_decode(self.request.body)
            print('going !! > ', query)
            start_time = time.time()
            prediction = FPGrowthService(query).get_response()
            print("--- %s seconds ---" % (time.time() - start_time))
            self.finish(json.dumps(prediction,default=json_util.default))
        except Exception as error:
            print(error)
        finally:
            return 
