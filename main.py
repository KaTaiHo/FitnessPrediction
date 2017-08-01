import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import style
import csv
import xlrd
style.use('ggplot')
from sklearn.cluster import KMeans
import os


def run(file_name = None):
    data_array = []

    if file_name is not None:
        wb = xlrd.open_workbook(os.path.dirname(os.path.realpath(__file__)) + '//' + str(file_name))
        sheet = wb.sheet_by_index(0)

        for rowx in range(1, sheet.nrows, 1):
            cols = sheet.row_values(rowx)
            for i in range(1, len(cols), 1):
                try:
                    cols[i] = int(cols[i].replace(',', ''))
                except: 
                    cols[i] = int(float(cols[i].replace(',', ''))*100)
            data_array.append(cols[1:6])

        print(data_array)
    else:
        data_array = aggregate_data()

    x = np.array(data_array)

    kmeans = KMeans(n_clusters=3)
    kmeans.fit(x)

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    print(centroids)
    print(labels)

    colors = ['g.','r.', 'y.']

    for i in range(len(x)):
        print('coordinate:', x[i])
        plt.plot(x[i][0], x[i][1], colors[labels[i]], markersize = 10)

    plt.scatter(centroids[:, 0], centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder= 10)

    if file_name is not None:
        plt.savefig(file_name.replace('.xls',''))
    else:
        plt.savefig('aggregated_data')

def aggregate_data():
    current_path = os.path.dirname(os.path.realpath(__file__))
    data_array = []

    for subdir, dirs, files in os.walk(current_path + '\\data'):
        for file in files:
            wb = xlrd.open_workbook(os.path.dirname(os.path.realpath(__file__)) + '\\data\\' + str(file))
            sheet = wb.sheet_by_index(0)

            for rowx in range(1, sheet.nrows, 1):
                cols = sheet.row_values(rowx)
                for i in range(1, len(cols), 1):
                    try:
                        cols[i] = int(cols[i].replace(',', ''))
                    except: 
                        cols[i] = int(float(cols[i].replace(',', ''))*100)
                data_array.append(cols[1:6])

    return data_array