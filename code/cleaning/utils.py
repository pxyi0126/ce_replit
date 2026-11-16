import pandas as pd
import numpy as np
import re

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
    df = standardize_name_fec(pd.read_csv(filename, sep="|", names=cols, encoding="latin-1"))
    df = df.to_csv(filepath, index=False)

def clean_fund(filename, filepath, year):
    df = pd.read_csv(filename, sep=",")
    df = df[df['year'] == year]
    df = df.to_csv(filepath, index=False)

#need a function to standardize the names
def standardize_name_fec(df):
    for i in range(len(df)):
        name = df.loc[i, 'CAND_NAME'].split(", ")
        df.loc[i, 'CAND_NAME'] = name[1] + " " + name[0]
    return df

# def standardize_name_fund(name, file, col_name):

#     return df

# def merger(fec, fund, filepath):
#     continue
# probably will have to center merge, because there are a lot of libertarians and other parties in the MEDSL data

