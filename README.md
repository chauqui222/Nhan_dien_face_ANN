# Calories_Burned_Prediction
This project for predicting burned calories or for predicting calories that will be burned. This project deployed by using flask.
## Used Libraries:
- Pandas
- Seaborn
- Matplotlib
- Sklearn
- Xgboost
- Joblib
- Warnings
## Project Summary
- Most of the data is numeric as numeric data represents 88.9% of the data.
- The average of burned calories in this data almost equal to 90 calories.
- EDA gives a report that there are strong positive correlation between some features and calories(Target feature).
- I dropped the User_ID feature as it is a useless feature.
- Getting the dummies very important for taking a real benefits from categorical data during machine learning model as i did with gender feature.
- Standard scaler helps to get standardized distribution, and gives us good results.
- From EDA, regression models will give a high accuracy, but the reasons to use XGBoost are execution speed and model performance.
- Mean absolute error(MAE) eaual to 1.42.
- Mean squared error(MSE) equal to 4.23.
- By using r2_score metric, accuracy almost equal to 100%.
