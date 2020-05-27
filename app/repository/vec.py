import sys
sys.path.append('./.')
from gensim.models import Word2Vec
import pandas as pd
import imutils
import cv2
import time

class VecRepository:         
    def get_associated_style_codes(self, list):
        result=None
        try:
            start_time = time.time()
            print("---start %s seconds ---" % (time.time() - start_time))
            model = Word2Vec.load("C:/work/data/model/word2vec.model")
            print("---load done %s seconds ---" % (time.time() - start_time))
            result = model.most_similar(positive=list, topn=5)
            print("NE>", result)
            print("---transform done %s seconds ---" % (time.time() - start_time))
        except Exception as error:
            print(error)
        finally:
            return result

    def get_img_from_codes(self, list_pids):
        result=None
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
    

