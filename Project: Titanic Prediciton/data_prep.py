import pandas  as pd

inputData = pd.read_csv('test.csv')

# print(type(inputData))

inputData = inputData.drop('Name',1)

#making dummy variables for sex and embark

data = pd.concat([inputData, pd.get_dummies(inputData['Sex'], prefix='Sex')], axis=1)
data = data.drop('Sex',axis=1)
data2 = pd.concat([data, pd.get_dummies(data['Embarked'], prefix='Embarked')], axis=1)



data2 = data2.drop('Embarked',axis=1)
#ticket ko theek krna h !!
for index, row in data2.iterrows():
    print(row['Ticket'])

# print(data2)
