import os
import sys 

import json
import pandas as pd

sys.path.insert(0, 'src')
from graphs-analysis import megabytes_graph
from data_clean import clean
from compute import mean,time_vs_bytes,max_bytes

def data():
    raw_path="notebooks/data/"
    lst_files=os.listdir(raw_path)
    return [pd.read_csv(f, low_memory=False) for f in lst_files]


def main(targets):

    data_config = json.load(open('config/data-params.json'))
    eda_config = json.load(open('config/config.json'))

    if "data" in target:
        
        data= data()        

    if 'clean' in targets:
        for x in range(len(data)):
            try:
                data_cleaner(x)
            except NameError:
                continue


    if 'analysis' in targets:
        for x in range(len(data)):
            megabytes_graph(x)
    
    if "compute" in targets:
        for x in range(len(data)):
            mean(x)
            time_vs_bytes(x)
            max_bytes(x)

        convert_notebook(**eda_config.json)

    




if __name__ == '__main__':
    targets=sys.argv[1:]
    main(targets)