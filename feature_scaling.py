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
        input_rawCSV[['sqft_living' , 'sqft_lot' , 'sqft_living15' , 'sqft_lot15']] = scaler.fit_transform(input_rawCSV[['sqft_living' , 'sqft_lot' , 'sqft_living15' , 'sqft_lot15']])
        return input_rawCSV,output_rawCSV







'''
id,date,price,bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade,sqft_above,sqft_basement,yr_built,yr_renovated,zipcode,lat,long,sqft_living15,sqft_lot15

root
 |-- id: long (nullable = true)
 |-- date: string (nullable = true)
 |-- price: decimal(7,0) (nullable = true)
 |-- bedrooms: integer (nullable = true)
 |-- bathrooms: double (nullable = true)
 |-- sqft_living: integer (nullable = true)
 |-- sqft_lot: integer (nullable = true)
 |-- floors: double (nullable = true)
 |-- waterfront: integer (nullable = true)
 |-- view: integer (nullable = true)
 |-- condition: integer (nullable = true)
 |-- grade: integer (nullable = true)
 |-- sqft_above: integer (nullable = true)
 |-- sqft_basement: integer (nullable = true)
 |-- yr_built: integer (nullable = true)
 |-- yr_renovated: integer (nullable = true)
 |-- zipcode: integer (nullable = true)
 |-- lat: double (nullable = true)
 |-- long: double (nullable = true)
 |-- sqft_living15: integer (nullable = true)
 |-- sqft_lot15: integer (nullable = true)
 '''