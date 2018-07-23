#!/usr/bin/python3
import pandas
import matplotlib.pyplot as plt
import math

##############
#Introduction#
##############
frames=[]
keys=[]
for i in range(2003,2009):
    #print("Year: ", i)
    comp = pandas.read_csv(str(i)+'.csv',sep='\t')
    comp['SALARY'] = comp['SALARY'].str.replace(',','').str.replace('$','').astype('float64')
    comp['YEAR'] = i
    #print(comp)
    frames.append(comp)
    #keys.append(str(i))
    #print(comp.describe())
    #comp.boxplot(ax=i)
for i in range(2009,2019):
    #print("Year: ", i)
    comp = pandas.read_csv(str(i)+'.csv',dtype={'SALARY': object})
    comp['SALARY'] = comp['SALARY'].str.replace(',','').str.replace('$','').astype('float64')
    comp['YEAR'] = i
    frames.append(comp)
    #frames.append(comp['SALARY'])
    #keys.append(str(i))
    #print(comp.describe())
    #comp.boxplot()
result = pandas.concat(frames)
#plt.show()
#all_frames = pandas.concat(frames,keys=keys)
#print(result[['YEAR','SALARY']])
result.boxplot(by=['YEAR'])
plt.title("Boxplot of White House Staff Salary by Year")
plt.show()

#comp = pandas.read_csv('2010.csv',sep='\t')
#comp['SALARY'] = comp['SALARY'].str.replace(',','').str.replace('$','').astype('float64')
#print(comp)
#print(comp.columns)
#print(comp.dtypes)
#print(comp.describe())

##########################################
#Find Unique Compliants with full records#
##########################################
#fullUniComp = uniComp.drop_duplicates(subset="UniqueComplaintId").count()
#print("Full records counted unique compliantID's: ", fullUniComp[1])
