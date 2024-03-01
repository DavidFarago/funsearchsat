import os
import subprocess
import cadopt
import time
import pandas as pd

def compute_number_rounds(feature_record: dict) -> int:
    """Extract the allowed features from the feature record and apply the heuristics to derive the optimal number of rounds.

    :param feature_record: A dict containing the features of a CNF file.
    :returns: the number of rounds to be used for the given feature record, between 0 and 50.
    """
    expected_keys = ['clauses', 'variables', 'cls1', 'cls2', 'cls3', 'cls4', 'horn', 'invhorn', 'positive', 'negative']
    assert all(key in feature_record for key in expected_keys), f"Expected keys: {expected_keys}, got: {feature_record.keys()}"
    return number_rounds_heuristic(**{key: feature_record[key] for key in expected_keys})

def number_rounds_heuristic(clauses: int, variables: int, cls1: int, cls2: int, cls3: int, cls4: int, horn: int, invhorn: int, positive: int, negative: int) -> int:
    """Derive the optimal number of rounds between 0 and 50 for the given features.

    :param clauses: The number of clauses in the CNF file.
    :param variables: The number of variables in the CNF file.
    :param cls1: The number of clauses of length 1.
    :param cls2: The number of clauses of length 2.
    :param cls3: The number of clauses of length 3.
    :param cls4: The number of clauses of length 4.
    :param horn: The number of Horn clauses.
    :param invhorn: The number of inverse Horn clauses.
    :param positive: The number of positive literals.
    :param negative: The number of negative literals.
    :returns: the number of rounds to be used for the given features, between 0 and 50.
    """
    return 0

def getcommand(featrec, fin, fout):
    nrounds = compute_number_rounds(featrec)
    cadopts = cadopt.getoptdict(featrec)
    command = [ './cadical/build/cadical', "-P{}".format(nrounds) ]
    ioparam = [ '-d', '0', '-o', fout, fin ]
    return command + [ "{}={}".format(k, v) for k, v in cadopts.items() ] + ioparam

def getfeatures(fin):
    data = pd.read_csv('feat.csv')
    hash = fin.split('-')[0]
    return data.query('hash == @hash').iloc[0].to_dict()

def runcadical(uncompressed_input_file):
    """
    Run cadical with the given input file and feature record.

    :param uncompressed_input_file: The filename of the _uncompressed_ input file.
    :returns: The percental reduction speed, i.e. percental size reduction per second.
    """
    features = getfeatures(uncompressed_input_file)
    command = getcommand(features, uncompressed_input_file, f'{uncompressed_input_file}.out.cnf')
    start = time.perf_counter()
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    seconds = time.perf_counter() - start
    assert result.returncode in [0, 10, 20], f"Unexpected return code '{result.returncode}' for {uncompressed_input_file}"

    if result.returncode == 10:
        reduction = 1
        reason = "SAT"
    elif result.returncode == 20:
        reduction = 1
        reason = "UNSAT"
    elif result.returncode == 0:
        input_size = os.stat(uncompressed_input_file).st_size
        output_size = os.stat(f'{uncompressed_input_file}.out.cnf').st_size
        assert output_size <= input_size
        reduction = (input_size - output_size) / input_size
        reason = f"input_size = {input_size} and output_size = {output_size}"
    print(f"Runtime for {uncompressed_input_file}: {seconds} seconds, percental_reduction = {reduction}, due to {reason}")
    return reduction / seconds
