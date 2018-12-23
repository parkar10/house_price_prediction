import pandas as pd
from data_preprocessing import DataPreprocessing
from sklearn.preprocessing import MinMaxScaler

class FeatureScaling:
    def getFeaturedDataframe(self):
        dp = DataPreprocessing()
        rawCSV = dp.getInputDataframe()
        output_rawCSV = rawCSV['price']
        input_rawCSV = rawCSV.drop(['id','date','price'], axis = 1)
        scaler = MinMaxScaler()
        scalar..partial_fit(input_rawCSV)
        input_rawCSV[['sqft_living' , 'sqft_lot' , 'sqft_living15' , 'sqft_lot15']] = scaler.ransform(input_rawCSV[['sqft_living' , 'sqft_lot' , 'sqft_living15' , 'sqft_lot15']])
        return input_rawCSV,output_rawCSV
