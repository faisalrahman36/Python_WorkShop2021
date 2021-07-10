import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  
from sklearn import metrics  

#Multiple linear regression 
#We want to predict hba1c with weight age height exercise calorie sleep triglycerides as independent variables

dataset = pd.read_csv('E:\Python_Programming_Course\Python2021\SciPy_Curve_fit_StatsModel_Sci-kit_multiple_Reg\hba1c_fake.csv')  
print(dataset.head(2))  
#describing data
print(dataset.describe())  
#preparing data

#Independent variables : WeightKg	HeightMeter	AgeYears	DailyExerciseHr	SleepHr	DailyCalorie	Triglycerides

X = dataset[['WeightKg', 'HeightMeter', 'AgeYears', 'SleepHr' ,'DailyCalorie','Triglycerides',
       'DailyExerciseHr']]
#dependent variable: hba1c which we want to predict
y = dataset['Hba1c'] 

#Execute the following code to divide our data into training and test sets:

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) 
regressor = LinearRegression()  
regressor.fit(X_train, y_train)  
coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])  
print('---coeff_df---')
print(coeff_df)
#making predictions
y_pred = regressor.predict(X_test) 
#comparison of prediction with actual
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
print(df)
#Error analysis
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))   
  