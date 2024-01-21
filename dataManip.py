import pandas as pd
#First Data

data ={'Name':['Shreyas','Gittu','Aai','Pappa'],'Age':[27,31,55,58]}
df = pd.DataFrame(data)
print('Data in Dataframe structure:',df)

#Second Data

data2 = ['JavaScript','Python','CSS','HTML','NodeJS']
s=pd.Series(data2)
print('Data in series data structure:',s)
print(s[1:3])

#Third Data

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

df2 = pd.DataFrame(x)
print(df2)