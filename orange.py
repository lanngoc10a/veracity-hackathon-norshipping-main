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
ship_info = pd.read_csv("doc/ships.csv")
ship_info["max_speed"]=15.5
ship_info["min_speed"]=6

cost_pr_tonnage={
    "2022":0,
    "2023":0.2,
    "2024":0.45,
    "2025":0.7,
    "2026":1,
    }
#%%
ship_info.columns = [header.replace(" ", "_") for header in ship_info.columns]
ship_info["Permissible_Intake"]
#%%Assumed values

#%%

solver = pw.Solver.CreateSolver('SCIP')
var = {}
constraint = {}
for v in range(len(ship_info)):
    ship=ship_info["imo"][v]
    var[ship]={
    "name":ship,
    "st":solver.NumVar(6, 16.5, 'sl_{}'.format(v)),
    "sr":solver.NumVar(6, 16.5, 'sl_{}'.format(v)),
    "t":solver.IntVar(0, ship_info["Permissible_I"][v], "T_{}".format(v)),
    "n":solver.IntVar(0,solver.infinity(), "n_{}".format(v) ),
    }
cons_in1 = solver.Constraint(-solver.infinity(), 50)
constraint = {}
for c in range(len(ship_info)):
    solver.add("s_{}".format(v), var[c]["s"]*var[c]["n"])
