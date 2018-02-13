import pandas  as pd
import re

inputData = pd.read_csv('test.csv')

def TicketTheekKrneWala():
    for index, row in data2.iterrows():
        str(data2["Ticket"][index])
        re.sub("\D","",data2["Ticket"][index])
        # print(ticket)



# print(type(inputData))

inputData = inputData.drop('Name',1)

#making dummy variables for sex and embark

data = pd.concat([inputData, pd.get_dummies(inputData['Sex'], prefix='Sex')], axis=1)
data = data.drop('Sex',axis=1)
data2 = pd.concat([data, pd.get_dummies(data['Embarked'], prefix='Embarked')], axis=1)



data2 = data2.drop('Embarked',axis=1)

data2.to_string(columns="Ticket")
#ticket ko theek krna h !!
TicketTheekKrneWala()

print(data2)
