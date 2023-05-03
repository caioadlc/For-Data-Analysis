#Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import chisquare

#Connect to google drive
#from google.colab import drive
#drive.mount('/content/drive')

df = pd.read_csv('./testes.csv')
#one=df.pop("Medida")#GET THE COLUMN THAT HAS THE NAME "MEDIDA"
df=df.drop(index=[3,4,5])
df1=df.to_numpy()#TAKE ALL FLOATTING-POINT VALUES OF DATA FRAME
print("Data Frame: ","\n",df,"\n","Pontos: ","\n",df1)


#Take data for plotting
x=[]
y=[]
for i in range(len(df1)):
    x.append(df1[i][0])
    y.append(df1[i][1])


#Fit and Uncertainty

#Function to be fit
def f(x, a, b):
    return a*x+b
sy=0.05
# Make a fit
p0 = [1, 1] # Initial Values
popt, pcov = curve_fit(f, x, y, p0) #popt adjust parameter 
#and pcov covariance matrix
perr = np.sqrt(np.diag(pcov)) #Get the values ​​of the pcov diagonal
x,y=np.array(x),np.array(y)#Convert list to array

#Print parameters
df=pd.DataFrame({'Value': popt, 'Uncertainty': perr},index=['a','b'])
print(df)

colors=['#9400D3','violet','blue']

#Settiings to plotting
plt.figure(figsize=(18,12))
plt.ylabel('$V_0$ (V)',fontsize=15)
plt.xlabel('$v$(THz)',fontsize=15)
plt.errorbar(x, y, yerr=sy, color='black', capsize=4,ls='',label='Incerteza') #Plot point and uncertainty
plt.scatter(x, y,s=350, marker='.',alpha=1,c=colors, label='Dados experimentais')
plt.plot(x, f(x, *popt), color='black', label='Ajuste Teórico') #Plot fit
plt.title('Tensão por Frequência',fontsize=30)
plt.legend(fontsize=15)
plt.show()

#Statistical tests

#Qui Square
#f_obs=fit function, f_exp=Experimental values,ddof=degrees of freedom
#chisquare(f_obs, f_exp=None, ddof=0)