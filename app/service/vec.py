import pandas as pd

from app.repository.vec import VecRepository
from app.model.vec import VecModel

class VecService:
    def __init__(self,query):
        self.query=query
        self.type = query['type']
        self.pid = query['pid']

    def get_response(self):
        result = {
            'code': lambda _: self.get_associated_style_codes(),
            'img': lambda _: self.get_img_from_codes(),
            'random': lambda _: self.get_random_prediction()
        }[self.type](self.query)
        return result

    def get_associated_style_codes(self):
        res= None
        try:
            _query = [str(i) for i in self.query['pid']]
            response = VecRepository().get_associated_style_codes(_query)
            success = True
            data = [int(i[0]) for i in response]
            message = 'Fetched associated style codes successfully'
            error =None
        except Exception as err:
            print('app >>',err)
            success = False
            data = None
            message = 'Failed to fetch associated style codes successfully'
            error = err
        finally:
            response = VecModel(success, data, error, message).get_response()
            return response

    def get_img_from_codes(self):
        res= None
        try:
            response = VecRepository().get_img_from_codes(self.pid)
            success = True
            data = response
            message = 'Fetched image links successfully'
            error = None
        except Exception as err:
            print('img >>',err)
            success = False
            data = None
            message = 'Failed to fetch img links successfully'
            error = err
        finally:
            res = VecModel(success, data, error, message).get_response()
            return res

    def get_random_prediction(self):
        res= None
        try:
            response = VecRepository().get_random_prediction(self.pid)

        except Exception as err:
            print('img >>',err)
            success = False
            data = None
            message = 'Failed to fetch imgs successfully'
            error = err
        finally:
            return res

