import pandas as pd

# dataframe
data = {
    'Name' : ['John','Anna','Peter','Linda'],
    'Age' : [28,34,29,32]
}
df = pd.DataFrame(data)

#Series 생성
ages = pd.Series([28,34,29,32], name='Age')
print(df)