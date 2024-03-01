import os
import subprocess
import cadopt
import time
import pandas as pd

def rounds(featrec):
    ncls = featrec['clauses']
    nvars = featrec['variables']
    ncls1 = featrec['cls1']
    ncls2 = featrec['cls2']
    ncls3 = featrec['cls3']
    ncls4 = featrec['cls4']
    ncls5 = featrec['cls5']
    ncls6 = featrec['cls6']
    ncls7 = featrec['cls7']
    ncls8 = featrec['cls8']
    ncls9 = featrec['cls9']
    ncls10p = featrec['cls10p']
    nhorn = featrec['horn']
    ninvhorn = featrec['invhorn']
    npos = featrec['positive']
    nneg = featrec['negative']
    return 0

def getcommand(featrec, fin, fout):
    nrounds = rounds(featrec)
    cadopts = cadopt.getoptdict(featrec)
    command = [ './cadical/build/cadical', "-P{}".format(nrounds) ]
    ioparam = [ '-d', '0', '-o', fout, fin ]
    return command + [ "{}={}".format(k, v) for k, v in cadopts.items() ] + ioparam

def getfeatures(fin):
    data = pd.read_csv('feat.csv')
    hash = fin.split('-')[0]
    return data.query('hash == @hash').iloc[0].to_dict()

# run cadical with the given input file and feature record
def runcadical(fin):
    featrec = getfeatures(fin)
    command = getcommand(featrec, fin, f'{fin}.out.cnf')
    start = time.perf_counter()
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    R = time.perf_counter() - start

    if result.returncode in [ 10, 20 ]:
        print("Command executed successfully.")
        return 1 / R
    elif result.returncode == 0:
        print("Command executed successfully.")
        szin = os.stat(fin).st_size
        szout = os.stat(f'{fin}.out.cnf').st_size
        Q = max(-1, (szin - szout) / szout)
        return Q / R
    else:
        print("Command failed with return code:", result.returncode)
        return -1