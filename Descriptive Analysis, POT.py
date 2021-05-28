##Python code (Times Series, Descriptive Analysis, POT)

#Import Modules import scipy.stats as stats import pandas as pd import researchpy as rp import statsmodels.api as sm from statsmodels.formula.api import ols import matplotlib.pyplot as plt import seaborn as sns import numpy as np from thresholdmodeling import thresh_modeling #importing package for POT
import scipy.stats as stats
import pandas as pd
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols  
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from thresholdmodeling import thresh_modeling #importing package for POT

##Import Data #Daily

dft = pd.read_excel('data/Temperature_d.xlsx')
dfv = pd.read_excel('data/sea_water_velocity_d.xlsx')
dfs = pd.read_excel('data/Salinity_d.xlsx')

#Montly

dftm = pd.read_excel('data/Temperature_m.xlsx')
dfsm = pd.read_excel('data/Salinity_m.xlsx')
dfn = pd.read_excel('data/Nitrate_m.xlsx')
dfpho = pd.read_excel('data/Phoshpare_m.xlsx')
dfc = pd.read_excel('data/Chlorophyle_m.xlsx')
dfphy = pd.read_excel('data/Phy_m.xlsx')
dfdo = pd.read_excel('data/DO_m.xlsx')

#Hourly

dfhmo = pd.read_excel('data/Hmo.xlsx')

#Graphs
import os
x = "Salinity"
if x == "Temperature":
    df = dft
    i = "[C˚]"
    time = 'Days'
elif x == "Salinity":
    df = dfs
    i = "[psu]"
    time = 'Days'
elif x == "Nitrate":
    df = dfn
    i = "[mmol m-3]"
    time = 'Months'
elif x == "Phosphorus":
    df = dfpho
    i = "[mmol m-3]"
    time = 'Months'
elif x == "Chlorophyll":
    df = dfc
    i = "[mg m-3]"
    time = 'Months'
elif x == "Phytoplankton":
    df = dfphy
    i = "[mmol m-3]"
    time = 'Months'
elif x == "Dissolved Oxygen":
    df = dfdo
    i = "[mmol m-3]"
    time = 'Months'
elif x == "Water Velocity":
    df =dfv
    i = "[m/s]"
    time = 'Days'
elif x == "Significant Wave Height":
    df = dfhmo
    i = "[m]"
    time = 'Hours'

#Tables
# dfc.corr()
# dft.describe()
    
#Time Series
# df[['ID278', 'ID298', 'ID276']].plot()
# df.plot(x='Time',y=['ID278', 'ID298','ID276'])
# plt.xlabel('Time [Year]')
# plt.ylabel(x + " " + i)
# plt.savefig(os.path.join('/Users/tdvr/Documents/Dissertation/Graphs/TimeSeries', x), dpi=200)

# #BoxPlot
df.boxplot()
#plt.title(x +" Boxplot")
plt.xlabel('Location')
plt.ylabel(x + " " + i)
plt.savefig(os.path.join('/Users/tdvr/Documents/Dissertation/Graphs/Boxplot', x), dpi=200)

# ##Density
# df[labels].plot.density()
# # plt.title(x)
# plt.xlabel(x + " " + i)
# plt.ylabel('[Frenquency %]')
# plt.savefig(os.path.join('/Users/tdvr/Documents/Dissertation/Graphs/Density', x), dpi=200)


# ###PairGrid

def corrfunc(x, y, **kws):
    (r, p) = stats.pearsonr(x, y)
    ax = plt.gca()
    ax.annotate("r = {:.2f} ".format(r),
                xy=(.1, .9), xycoords=ax.transAxes)
   # ax.annotate("p = {:.3f}".format(p),
    #            xy=(.4, .9), xycoords=ax.transAxes)

# g = sns.pairplot(dfp, vars=['ID003','ID008','ID032', 'ID046'], kind='reg', diag_kind="kde")
g = sns.PairGrid(df, vars=['ID046','ID278', 'ID298'])
g.fig.suptitle(x + " " + i, y=1.04, fontsize=18)
# g.map_upper(plt.scatter, s=10)
# g.map_diag(sns.distplot, kde=False)
g.map_upper(sns.scatterplot, size=40)
g.map_diag(sns.distplot, kde=True, color=None)
# g.map_diag(sns.kdeplot)
g.map_lower(sns.kdeplot, cmap="Oranges_r")
g.map_lower(corrfunc)


###POT

data = pd.read_excel('data/Hmo.xlsx')
potdata= data.drop(['Time'], axis=1)
potdata = data['ID032'].values.ravel()
u=3.5 #u varies per site
potdata

#Hourly

potdata= data.drop(['Time'], axis=1)

potdata = data['ID032'].values.ravel() u=3.5 #threshold[m] potdata

#P-P Plot
thresh_modeling.ppplot(potdata, u, 'mle', 0.05)

#Return Value Analysis
thresh_modeling.return_value(potdata, u, 0.05, 8760, 876000, 'mle')

#Declustering
thresh_modeling.decluster(potdata, u, 720) 
