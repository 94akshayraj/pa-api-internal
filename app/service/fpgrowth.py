import pandas as pd

from app.repository.fpgrowth import FPGrowthRepository
from app.model.fpgrowth import FPGrowthModel

class FPGrowthService:
    def __init__(self,query):
        self.query=query
        print("herer >> ", query)
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
            pandas_df = pd.DataFrame([[_query]], columns=['transaction'])
            
            response = FPGrowthRepository().get_associated_style_codes(pandas_df)
            success = True
            data = [int(i) for i in response['prediction'][0]]
            message = 'Fetched associated style codes successfully'
            error =None
        except Exception as err:
            print('app >>',err)
            success = False
            data = None
            message = 'Failed to fetch associated style codes successfully'
            error = err
        finally:
            response = FPGrowthModel(success, data, error, message).get_response()
            return response

    def get_img_from_codes(self):
        res= None
        try:
            response = FPGrowthRepository().get_img_from_codes(self.pid)
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
            res = FPGrowthModel(success, data, error, message).get_response()
            return res

    def get_random_prediction(self):
        res= None
        try:
            response = FPGrowthRepository().get_random_prediction(self.pid)

        except Exception as err:
            print('img >>',err)
            success = False
            data = None
            message = 'Failed to fetch imgs successfully'
            error = err
        finally:
            return res

