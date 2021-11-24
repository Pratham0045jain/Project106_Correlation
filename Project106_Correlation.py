import csv
import plotly_express as px
import numpy as np

""" with open("Data/Ice-Cream vs Temperature data.csv") as file1:
    df1 = csv.DictReader(file1)
    scatter_graph1 = px.scatter(df1, x="Temperature", y="Ice-cream Sales")
    scatter_graph1.show() """


def get_data_source(data_path):

    list1 = []
    list2 = []

    with open(data_path) as file1:
        df1 = csv.DictReader(file1)

        col1 = (input("enter col1 name "))
        dataType1 = type(col1)

        col2 = (input("enter col2 name "))
        dataType2 = type(col2)

        print(dataType1)
        print(dataType2)

        for row in df1:
            list2.append(float(row[col1]))
            list1.append(float(row[col2]))

    return{"x": list1, "y": list2}


def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print(correlation[0, 1])


def setup():
    data_path = input("Enter the path ")

    data_source = get_data_source(data_path)
    findCorrelation(data_source)


setup()

""" with open("Data\coffee vs hours of sleep.csv") as file2:
    df2 = csv.DictReader(file2)
    scatter_graph2 = px.scatter(df2, x="sleep in hours", y="Coffee in ml")
    scatter_graph2.show() """
