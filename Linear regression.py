# -*- coding:utf-8 -*-
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np


# Load Data
def loadDataSet(fileName):

    numFeat = len(open(fileName).readline().split('\t')) - 1
    xArr = [];
    yArr = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        xArr.append(lineArr)
        yArr.append(float(curLine[-1]))
    return xArr, yArr


def rssError(yArr, yHatArr):

    return ((yArr - yHatArr) ** 2).sum()

# Calculate regression coefficient
def standRegres(inxMat, inyMat):

    xMat = np.mat(inxMat);
    yMat = np.mat(inyMat).T
    xTx = xMat.T * xMat
    print(xTx)
    if np.linalg.det(xTx) == 0.0:
        print("error")
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws


# Use linear regression
def useStandRegres():

    xArr, yArr = loadDataSet('data01.txt')
    ws = standRegres(xArr, yArr)
    xMat = np.mat(xArr)
    yMat = np.mat(yArr)
    yHat = xMat * ws
    print(np.corrcoef(yHat.T, yMat))
    print(ws[0],ws[1],ws[2],ws[3],ws[4],ws[5],ws[6],ws[7],ws[8],ws[9],ws[10])

if __name__ == '__main__':
    useStandRegres()