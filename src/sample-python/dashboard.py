import dash
from dash import dcc
from dash import html
import plotly.express as px
# Input data files are available in the "../input/" directory.
import os
import matplotlib.pyplot as plt#visualization
from PIL import  Image
import seaborn as sns#visualization
import itertools
import warnings
warnings.filterwarnings("ignore")
import io
import plotly.offline as py#visualization
import plotly.graph_objs as go#visualization
import plotly.tools as tls#visualization
import plotly.figure_factory as ff#visualization
import os
import plotly.graph_objs as go
import numpy as np

class Dashboard:
     """
    Dashboard!
    """

    # SMALL_SIZE = dict(width=400, height=300)
    # MEDIUM_SIZE = dict(width=600, height=400)
    # WIDE_SIZE = dict(width=600, height=300)
    # EXTRA_WIDE_SIZE = dict(width=800, height=300)
     #self.df = df
    #self.df = pd.read_csv("result.csv")

   #   @property
   #   def T1s(df):
   #      return df.imo.unique()
 