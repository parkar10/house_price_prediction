#"ISBN" "Book-Title";"Book-Author";"Year-Of-Publication";"Publisher";"Image-URL-S";"Image-URL-M";"Image-URL-L"
import pandas as pd


class DataPreprocessing:

    def getInputDataframe(self):
        rawCSV = pd.read_csv("dataset/house_data.csv")
        return rawCSV
        