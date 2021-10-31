import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Coffee_in_ml", y="sleep_in_hours")
        fig.show()

def getdatasource(datapath):
    Coffee_in_ml=[]
    sleep_in_hours=[]
    with open(datapath)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            Coffee_in_ml.append(float(row["Coffee_in_ml"]))
            sleep_in_hours.append(float(row["sleep_in_hours"]))
    return {"x":Coffee_in_ml,"y":sleep_in_hours}

def findcorrelation (datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation is ",correlation[0,1])

def setup ():
    datapath="coffee.csv"
    datasource=getdatasource (datapath)
    findcorrelation(datasource)
setup()