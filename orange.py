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
#Cleaning
os.chdir(r"C:\Users\Tormo\OneDrive\Skrivebord\schule\competitions\teamorange")
df = pd.read_csv("doc/ships.csv")
df.info()
df.drop(df.columns[[3]], axis=1, inplace=True)
df.columns = [header.replace(" ", "_").lower() for header in df.columns]
df = df[["imo", "grain_capacity", "max_intake", "permissible_intake", "permissible_dwt", "permissible_dwt", "dwt", "dwcc", "t", "tpc", "type"]]
#
float_columns = ["max_intake", "dwcc", "dwt", "permissible_intake", "permissible_dwt", "grain_capacity"]
string_columns = ["type", "built_country", "fuel"]
df[float_columns]=df[float_columns].apply(lambda x: x.str.replace(',','.'))
df[float_columns]=df[float_columns].astype("float64")
df[string_columns]=df[string_columns].astype("string")
df.reset_index(inplace=True)


#%%

#Speed in nautical
max_speed=15.5
min_speed=6
#Tons of soy
tonnage=2,5*1000000
#in nautical miles
distance = 5116000
#years
years = 5
#Max travel time per ship
max_time = years*365*24


emission_costs={
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
#Min tonnage transport
solver.Add(sum([var["t"]])>=tonnage)

for c in range(len(df)):
    
    mx_dwt = df["permissible_dwt"]
    mx_ton = df["permissible_intake"]
    mx_vol = df["grain_capacity"]
    
    hs = var[c]["hs"]
    hr = var[c]["hr"]
    t =  var[c]["t"]
    n =  var[c]["n"]
    #Time spent per ship
    solver.Add("t_{}".format(c), (5+hs+5+hr)*n<=max_time)
    #Max DWT per per trip
    solver.Add("t_{}".format(c), 