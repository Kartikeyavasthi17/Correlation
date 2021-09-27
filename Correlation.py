import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    Marks_in_percentage = []
    DaysPresent = []
    with open(data_path)as f:
        f_reader = csv.DictReader(f)
        for row in f_reader:
            Marks_in_percentage.append(float(row["Marks_in_percentage"]))
    return{"x":Marks_in_percentage,"y":DaysPresent}


    def findCorrelation(datasource):
        correlation = np.corrcoef(datasource["x"],datasource["y"])  
        print("Students_Marks vs Days of Present: \n==>",correlation[0,1])





    def setup():
        data_path = "Students_Marks vs Days of Present.csv"
        
        
        datasource = getDataSource(data_path)
        findCorrelation(datasource)         



setup()