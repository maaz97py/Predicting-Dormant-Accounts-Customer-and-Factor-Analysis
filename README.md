# Predicting-Dormant-Accounts-Customer-and-Factor-Analysis

## What is a dormant Account?
Before finding out the factors influencing dormancy it is important to understand the definition of a dormant account. Let me make it simple for you. 
When an account has no transactions for 12 months, it is considered inactive. If there is no activity for 24 months, it is deemed dormant. Remember,
system-generated activities like interest credits don't count. A “transaction” is an activity initiated by the account holder

## why is it important to predict Dormant Customers?

In any banking environment dormant accounts are associated with lot of vulnerabilities such as maintaining such accounts which increases the overall expenses of the bank, 
risk of fraud and money laundering as the account is left unattended. To put it simply the cost of reviving existing customers is lower than acquiring new one's.

## Machine learning process.
![](https://github.com/maaz97py/Predicting-Dormant-Accounts-Customer-and-Factor-Analysis/blob/master/images1/image.png)

## Data collection .
* We collected primary data through online surveys.
* there are total 37 features in our data.
* We collected total of 1092 observations.

## Exploratory Data Analysis!
* our output variable is 'Current_satus'.
* it is a caegorical variabe with three categories 'active', 'inactive', 'Dormant'.
* Here are some of the visualizations involving our output variable and other independent variables.
![](https://github.com/maaz97py/Predicting-Dormant-Accounts-Customer-and-Factor-Analysis/blob/main/images2/image.png)
* Heatmap
![](https://github.com/maaz97py/Predicting-Dormant-Accounts-Customer-and-Factor-Analysis/raw/main/images3/image.png)
* all the values less than .5 are not related

## Feature Engineering!
* Dropped selected features based on hypothesis testing.
* Used Recursive Feature Elimination on categorical variables.
* and Anova test on Numerical variables
* Selected features are: Age,Gender,Education,Occupation,Account Type,Having Min Balance,Multiple Accounts,Active Loan,Internet/Mobile Banking,Credit Card,Whether defaulted Loan,Customer Service Satisfaction,Transaction done in 24 month,Opening Balance,Current Balance,Distance from Bank,Quarterly Activity Rate(no of transactions in 3 month),Current Status of your accounts [Active, Dormant, Inactive] - Output Variable .

## Model Building.
*  We experimentd with different machine learning models.
*  We tried different models using a library called 'Lazyclassifier'.
*  Here are the results
![](https://github.com/maaz97py/Predicting-Dormant-Accounts-Customer-and-Factor-Analysis/raw/main/images%204/image.png)
* We selected 'Random Forest' as it gave the best F1 score.

## Deployement.
*We did our model deployment using Flask API.
![](https://user-images.githubusercontent.com/69073502/117413310-71a89a80-af33-11eb-8267-eb56f7ab76ba.png)
