#load feature
# new_transformer = TfidfTransformer()
# loadVec = CountVectorizer(decode_error="replace", vocabulary=pickle.load(open("feaute.pkl", "rb")))
# tfidf_test = new_transformer.fit_transform(loadVec.fit_transform(["fuck you bitch, you are such a bitch idot!"]))
import grpc
from CommentDetector_pb2 import MsgRequest, MsgResponse
from CommentDetector_pb2_grpc import BullyingDetectionServiceServicer, BullyingDetectionServiceStub
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pickle
import joblib

class Detector(BullyingDetectionServiceServicer):
    def detectComment(self, request, context):
        print("Detector: "+str(request))
        labels_map = {0:"religion", 1:"age", 2:"gender", 3:"ethnicity", 4:"not_cyberbullying"}
        transformedInput = self.trasformInput(str(request.message))
        predictor = self.loadPreTrainedBullyingModel()
        predict_result = predictor.predict(transformedInput)
        if predict_result[0] != 4:
            return MsgResponse(response="is_cyberbullying")
        return MsgResponse(response=str(labels_map[predict_result[0]]))
    
    def trasformInput(self, input):
        transformer = TfidfTransformer()
        loadVec = CountVectorizer(decode_error="replace", vocabulary=pickle.load(open("featute.pkl", "rb")))
        tfidf = transformer.fit_transform(loadVec.fit_transform([input]))
        return tfidf
    
    def loadPreTrainedBullyingModel(self):
        loaded_model = joblib.load('random_forest.joblib')
        return loaded_model;

class ApiClient:
    def __init__(self, target):
        channel = grpc.insecure_channel(target)
        self.client = BullyingDetectionServiceStub(channel) 
    def detectComment(self, name):
        print("apiClient: "+name)
        response = self.client.detectComment(MsgRequest(message=name))
        return response
    