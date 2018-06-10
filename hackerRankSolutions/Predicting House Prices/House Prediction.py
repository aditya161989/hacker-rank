
# Import required packages
import re
import pandas as pd
import math
from sklearn.linear_model import LinearRegression

# Get initial inputs - The number of examples and features respectively
arr = input()
arr = re.sub('/\s/ig', ' ', arr)
input_data = list(map(int,arr.split(' ')))
train_data = []

# Input training data
for i in range(input_data[1]):
    val = input()
    val = re.sub('/\s/ig', ' ' , val)
    example = list(map(float,val.split(' ')))
    train_data.append(example)

# Separate features and expected output
train_data1 = pd.DataFrame(train_data)
X = train_data1.iloc[:,:-1]
y = train_data1.iloc[:,-1]

# Input the number of test data
arr = input()
arr = re.sub('/\s/ig', ' ', arr)
input_data = list(map(int,arr.split(' ')))
pred_data = []

# Import test data
for i in range(input_data[0]):
    val = input()
    val = re.sub('/\s/ig', ' ' , val)
    example = list(map(float,val.split(' ')))
    pred_data.append(example)


# Instantiate linear regression from sklearn
regressor = LinearRegression()
regressor.fit(X,y)
y_pred = regressor.predict(pred_data)

# Print output in required format
for i in range(len(y_pred)):
    output = math.ceil(y_pred[i]*100)/100
    print(output)


