import sys
sys.path.append('./.')
import findspark
findspark.init()
from pyspark.ml.fpm import FPGrowthModel
from pyspark.sql import SparkSession
import pandas as pd
import imutils
import cv2
import time

class FPGrowthRepository:
    def get_associated_style_codes(self, pandas_df):
        result=None
        try:
            start_time = time.time()
            print("START >>>")
            sess = SparkSession.builder.master("local").appName(
                "Product Association").config("spark.some.config.option", "some-value").getOrCreate()
            print("ENDDD >>>")
            pyspark_df = sess.createDataFrame(pandas_df)
            print("2 ENDDD >>>", pyspark_df.show())
            model = FPGrowthModel.load('C:/work/data/pa-model/pa1.0.0')
            print("3 ENDDD >>>")
            result = model.transform(pyspark_df).toPandas()
            print("wohooOOOOO >>>>",result)
        except Exception as error:
            print("exxece",error)
        finally:
            return result
    def get_img_from_codes(self, list_pids):
        result=None
        print('paas', list_pids)
        images_list = []
        try:
            start_time = time.time()

            data=pd.read_csv(r'C:/work/data/ace_pid_link.csv', usecols=['pid','link'])
            for i in list_pids:
                url = data.loc[data['pid'] == i, 'link'].iloc[0]
                images_list.append(url)
            print(len(images_list))
            # imutils.url_to_image(url)
            # montages = imutils.build_montages(images_list, (250, 250), (2, 1))
            # print("--- %s seconds ---" % (time.time() - start_time))
            # for montage in montages:
            #     cv2.imshow("Montage", montage)
            #     cv2.waitKey(0)
            #     cv2.destroyAllWindows()
            result = images_list
        except Exception as error:
            print(error)
        finally:
            return result
    

