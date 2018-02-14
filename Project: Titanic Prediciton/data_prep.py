import pandas  as pd
# import re
import string

class Del:
  def __init__(self, keep=string.digits):
    self.comp = dict((ord(c),c) for c in keep)
  def __getitem__(self, k):
    return self.comp.get(k)

DD = Del()
inputData = pd.read_csv('test.csv')

def TicketTheekKrneWala():
    for index, row in data2.iterrows():

        # re.sub("\D","",ticket)

        str(data2["Ticket"][index]).translate(DD)
        print(data2["Ticket"])




# print(type(inputData))

inputData = inputData.drop('Name',1)

#making dummy variables for sex and embark

data = pd.concat([inputData, pd.get_dummies(inputData['Sex'], prefix='Sex')], axis=1)
data = data.drop('Sex',axis=1)
data2 = pd.concat([data, pd.get_dummies(data['Embarked'], prefix='Embarked')], axis=1)



data2 = data2.drop('Embarked',axis=1)

# data2.to_string(columns="Ticket")
#ticket ko theek krna h !!


TicketTheekKrneWala()

# print(data2)
