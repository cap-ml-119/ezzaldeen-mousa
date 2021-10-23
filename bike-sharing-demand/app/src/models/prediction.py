import pickle
import numpy as np


class LRModel():
   # load the pickle file
    _model = pickle.load(open('./models/model.sav', 'rb'))

    def simple_prediction(self, sample):
        return self._model.predict(np.array(sample, ndmin=2))
