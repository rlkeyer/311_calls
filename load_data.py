# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 20:58:01 2018

@author: Rob
"""

import sqlite3 as sqlite
import pandas as pd

dat = pd.read_csv('./citizen311data_2016_0.csv')

dat.to_sql("data_311", sqlite.connect("metro_311.db"), index=False)