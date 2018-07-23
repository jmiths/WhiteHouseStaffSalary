#!/usr/bin/python3
import pandas
import matplotlib.pyplot as plt

inflation = { # Convert to 2018 dollars
        2003:1.3695,
        2004:1.3340,
        2005:1.2903,
        2006:1.2499,
        2007:1.2153,
        2008:1.1704,
        2009:1.1746,
        2010:1.1556,
        2011:1.1203,
        2012:1.0975,
        2013:1.0817,
        2014:1.0644,
        2015:1.0632,
        2016:1.0499,
        2017:1.0294,
        2018:1.0000
        }
frames=[]
keys=[]
mean=[]
median=[]
year=[]
for i in range(2003,2009):
    comp = pandas.read_csv(str(i)+'.csv',sep='\t')
    comp['SALARY'] = comp['SALARY'].str.replace(',','').str.replace('$','').astype('float64')
    comp['YEAR'] = i
    median.append(comp['SALARY'].median()*inflation[i])
    mean.append(comp['SALARY'].mean()*inflation[i])
    year.append(i)
    frames.append(comp)
for i in range(2009,2019):
    comp = pandas.read_csv(str(i)+'.csv',dtype={'SALARY': object})
    comp['SALARY'] = comp['SALARY'].str.replace(',','').str.replace('$','').astype('float64')
    comp['YEAR'] = i
    median.append(comp['SALARY'].median()*inflation[i])
    mean.append(comp['SALARY'].mean()*inflation[i])
    year.append(i)
    frames.append(comp)
result = pandas.concat(frames)
all_frames = pandas.concat(frames,keys=year)
''' First Graph 
result.boxplot(by=['YEAR'])
plt.title("Boxplot of White House Staff Salary by Year")
plt.show()
'''

''' Second Graph
plt.plot(year,mean)
plt.plot(year,median)
plt.xlabel("Year")
plt.ylabel("Salary(USD) 1e7")
plt.title("Mean and median White House Staff Salary adjust for inflation")
plt.legend(["Mean","Median"])
plt.show()
'''
