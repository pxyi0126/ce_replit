import pandas as pd
import numpy as np
import re
import os

def clean_fec(filename, filepath):
    cols = [
        "CAND_ID", "CAND_NAME", "CAND_ICI", "PTY_CD", "CAND_PTY_AFFILIATION",
        "TTL_RECEIPTS", "TRANS_FROM_AUTH", "TTL_DISB", "TRANS_TO_AUTH",
        "COH_BOP", "COH_COP", "CAND_CONTRIB", "CAND_LOANS", "OTHER_LOANS",
        "CAND_LOAN_REPAY", "OTHER_LOAN_REPAY", "DEBTS_OWED_BY", "TTL_INDIV_CONTRIB",
        "CAND_OFFICE_ST", "CAND_OFFICE_DISTRICT", "SPEC_ELECTION", "PRIM_ELECTION",
        "RUN_ELECTION", "GEN_ELECTION", "GEN_ELECTION_PRECENT",
        "OTHER_POL_CMTE_CONTRIB", "POL_PTY_CONTRIB", "CVG_END_DT",
        "INDIV_REFUNDS", "CMTE_REFUNDS",
    ]
    df = pd.read_csv(filename, sep="|", names=cols, encoding="latin-1")
    df = df.to_csv(filepath, index=False)

def clean_fund(filename, filepath, year):
    df = pd.read_csv(filename, sep=",")
    df = df[df['year'] == year]
    df = df.to_csv(filepath, index=False)

#need a function to standardize the names
def stand_fec(csv_file):
    df = pd.read_csv(csv_file)
    for i in range(len(df)):
        name = str(df.loc[i, 'CAND_NAME']).strip().split(", ")
        if len(name) >= 2:
            df.loc[i, 'CAND_NAME'] = name[1] + " " + name[0]
        else:
            df.loc[i, 'CAND_NAME'] = " ".join(name)
    df = df.to_csv(csv_file, index=False)

def stand_fund(csv_file):
    df = pd.read_csv(csv_file)
    for i in range(len(df)):
        if '\"' in df.loc[i, 'candidate']:
            name = re.sub(r'\\', '', df.loc[i, 'candidate'])
        else:
            name = df.loc[i, 'candidate']
        df.loc[i, 'candidate'] = name
    df = df.to_csv(csv_file, index=False)

# def merger(fec, fund, filepath):
#     continue
# probably will have to center merge, because there are a lot of libertarians and other parties in the MEDSL data

