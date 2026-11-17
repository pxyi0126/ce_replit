import numpy as np
import pandas as pd
from utils import *
import re

#for 1998
clean_fec("/users/yipho/utexas/381_final/data/raw/weball98.txt", "/users/yipho/utexas/381_final/data/intermediate/98fec.csv")
clean_fund("/users/yipho/utexas/381_final/data/raw/1976-2024-house.tab", "/users/yipho/utexas/381_final/data/intermediate/98fund.csv", 1998)
stand_fec("/users/yipho/utexas/381_final/data/intermediate/98fec.csv")
stand_fund("/users/yipho/utexas/381_final/data/intermediate/98fund.csv")

#for 2000
clean_fec("/users/yipho/utexas/381_final/data/raw/weball00.txt", "/users/yipho/utexas/381_final/data/intermediate/00fec.csv")
clean_fund("/users/yipho/utexas/381_final/data/raw/1976-2024-house.tab", "/users/yipho/utexas/381_final/data/intermediate/00fund.csv", 2000)
stand_fec("/users/yipho/utexas/381_final/data/intermediate/00fec.csv")
stand_fund("/users/yipho/utexas/381_final/data/intermediate/00fund.csv")
