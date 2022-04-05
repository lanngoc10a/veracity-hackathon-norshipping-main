# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 11:37:47 2022

@author: Tormo
"""
import os
import pandas as pd
import pandas_datareader as pdr
from ortools.linear_solver import pywraplp as pw
#%%
"""
Assumption Constraint: Equal tonnage per trip
"""

os.chdir(r"C:\Users\Tormo\OneDrive\Skrivebord\schule\competitions\teamorange")
df = pd.read_csv("doc/ships.csv")
print(df.info())
df.columns = [header.replace(" ", "_").lower() for header in df.columns]
float_columns = ["max_intake", "dwcc", "dwt", "permissible_intake", "permissible_dwt", "grain_capacity"]
string_columns = ["type", "built_country", "fuel"]
df[float_columns]=df[float_columns].apply(lambda x: x.str.replace(',','.'))
df[float_columns]=df[float_columns].astype("float64")
df[string_columns]=df[string_columns].astype("string")
df.drop(df.columns[[4]], axis=1, inplace=True)
df.reset_index(inplace=True)

#%%


df["max_speed"]=15.5
df["min_speed"]=6

df[[]]
distance = 5116000
max_time = 365*24
cost_pr_tonnage={
    "2022":0,
    "2023":0.2,
    "2024":0.45,
    "2025":0.7,
    "2026":1,
    }
#%%Assumed values

"""
hs-Hours per shippment trip
hr-Hours per return trip
t-tonns per shipment
n-number of trips
"""
solver = pw.Solver.CreateSolver('SCIP')
var = {}
constraint = {}
#%%
for v in range(len(df)):
    ship=df["imo"][v]
    var[ship]={
    "name":ship,
    "hs":solver.NumVar(6, 16.5, 'sl_{}'.format(v)),
    "hr":solver.NumVar(6, 16.5, 'sl_{}'.format(v)),
    "t":solver.NumVar(0, df["permissible_intake"][v], "T_{}".format(v)),
    "n":solver.NumVar(0,solver.infinity(), "n_{}".format(v)),
    }
constraint = {}
#%%
for c in range(len(df)):
    
    hs = distance/var[c]["hs"]
    hr = distance/var[c]["hr"]
    t =  distance/var[c]["t"]
    n =  var[c]["n"]
    #Time
    solver.Add("h_{}".format(c), (5+hs+5+hr)*n<=max_time)
    solver.Add("s_{}".format(c), distance/var[c]["h"]*var[c]["n"]<=max_time)