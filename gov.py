#!/usr/bin/python3
import pandas
import matplotlib.pyplot as plt

inflation = { # Convert to 2018 dollars
        2003:136.95,
        2004:133.40,
        2005:129.03,
        2006:124.99,
        2007:121.53,
        2008:117.04,
        2009:117.46,
        2010:115.56,
        2011:112.03,
        2012:109.75,
        2013:108.17,
        2014:106.44,
        2015:106.32,
        2016:104.99,
        2017:102.94,
        2018:100.00
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
all_frames = pandas.concat(frames,keys=keys)
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
