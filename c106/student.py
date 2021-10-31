import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
        fig.show()

def getdatasource(datapath):
    dayspresent=[]
    percentage=[]
    with open(datapath)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            dayspresent.append(float(row["Days Present"]))
            percentage.append(float(row["Marks In Percentage"]))
    return {"x":dayspresent,"y":percentage}

def findcorrelation (datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation is ",correlation[0,1])

def setup ():
    datapath="Student Marks vs Days Present.csv"
    datasource=getdatasource (datapath)
    findcorrelation(datasource)
setup()