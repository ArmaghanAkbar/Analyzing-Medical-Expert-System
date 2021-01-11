import pandas as pd 
import matplotlib.pyplot as plt

#read cvs file 
df = pd.read_csv("Covid Dataset.csv",nrows=1000)


#removing unuseful information 
df1=df.drop(columns=['Wearing Masks', 'Sanitization from Market'])

df1.to_csv("Covid Dataset1.csv",index =False)

df2=df.drop(columns=['Wearing Masks','Sanitization from Market','Asthma','Chronic Lung Disease','Headache','Heart Disease','Diabetes','Hyper Tension','Fatigue','Gastrointestinal ','Abroad travel','Contact with COVID Patient','Attended Large Gathering','Visited Public Exposed Places','Family working in Public Exposed Places'])
df2.to_csv("Bayesian.csv",index =False)
print('hello ')
#df2=df.drop(columns=['Wearing Mask','Sanitization from Market','Asthma','Chronic Lung Disease','Headache','Heart Disease','Diabetes','Hyper Tension','Fatigue','Gastrointestinal','Abroad travel','Contact with COVID Patient','Attended Large Gathering','Visited Public Exposed Places','Family working in Public Exposed Places'])
