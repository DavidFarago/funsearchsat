#!/usr/bin/env python3

import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def scatter(files, cfunc, clabel):
    markers = [ 'x', '+', '.', '2', '4', '_' ]
    for i, file in enumerate(files):
        data = pd.read_csv(file, names=['hash', 'result', 'isize', 'osize', 'time'])
        plt.scatter(data.iloc[:, 2], data.iloc[:, 3], marker=markers[i % len(markers)], label=file, c=cfunc(data.iloc[:, 2], data.iloc[:, 3], data.iloc[:, 4], data.iloc[:, 1]), cmap='plasma', linewidths=1) #cmap='coolwarm')#cmap='gist_heat')

    plt.colorbar(label=clabel, orientation='vertical')
    m = max(data.iloc[:, 2].max(), data.iloc[:, 3].max())
    plt.plot([1, m], [1, m], 'm:', linewidth=1) # diagnoal line
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Input Size')
    plt.ylabel('Output Size')
    plt.legend()
    plt.savefig(clabel + '.png')
    plt.show()

# reduction relative to input size
def relred(isize, osize, time, result):
    # change output size to 1 if instance is solved
    osize = np.where(result != "UNKNOWN", 1, osize)
    return (1 - (osize / isize))

# nonrelative reduction speed
def redspeed(isize, osize, time, result):
    # change output size to 1 if instance is solved
    osize = np.where(result != "UNKNOWN", 1, osize)
    return (isize - osize) / time

# score variant 1
def score(isize, osize, time, result):
    # change output size to 1 if instance is solved
    osize = np.where(result != "UNKNOWN", 1, osize)
    # set minimum to -1 and shift by 1 to get values between 0 and 2
    reduction = (np.maximum(-1, (1 - (osize / isize))) + 1)
    # divide by runtime
    return reduction / (time + 1)

def score2(isize, osize, time, result):
    # change output size to 1 if instance is solved
    osize = np.where(result != "UNKNOWN", 1, osize)
    # set minimum to -1 and shift by 1 to get values between 0 and 2
    reduction = (np.maximum(-1, (1 - (osize / isize))) + 1)
    # divide by log of runtime
    return reduction / np.log(time + math.e)

def score3(isize, osize, time, result):
    # change output size to 1 if instance is solved
    osize = np.where(result != "UNKNOWN", 1, osize)
    # set minimum to -1 and shift by 1 to get values between 0 and 2
    # use log of input size as exponent of relative reduction (=increases relative reduction score for larger instances)
    reduction = np.maximum(-1, (1 - np.power((osize / isize), np.log(isize)))) + 1
    # calculate runtime score between 1 and 2
    runtime = 2 - 1 / np.log(time + math.e)
    # divide reduction by runtime score
    return reduction / runtime

def main():
    parser = argparse.ArgumentParser(description='Process CSV files.')
    parser.add_argument('files', nargs='+', help='CSV files to process')
    args = parser.parse_args()

    scatter(args.files, relred, 'RelRed')
    scatter(args.files, relred, 'RedSpeed')
    scatter(args.files, score, 'Score')
    scatter(args.files, score2, 'Score2')
    scatter(args.files, score3, 'Score3')

if __name__ == "__main__":
    main()