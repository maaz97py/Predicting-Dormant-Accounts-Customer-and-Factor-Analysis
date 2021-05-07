# Predicting-Dormant-Accounts-Customer-and-Factor-Analysis

##  What is a Dormant Account?

Before finding out the factors influencing dormancy it is important to understand the definition of a dormant account. Let me make it simple for you. When an account has no transactions for 12 months, it is considered inactive. If there is no activity for 24 months, it is deemed dormant. Remember, system-generated activities like interest credits don't count. A “transaction” is an activity initiated by the account holder.

##  Why is it important to Predict Dormant Customers?

In any banking environment dormant accounts are associated with lot of vulnerabilities such as maintaining such accounts which increases the overall expenses of the bank, risk of fraud and money laundering as the account is left unattended.
To put it simply the cost of reviving existing customers is lower than acquiring new one's.

## The machine learning process.
![](https://github.com/maaz97py/Predicting-Dormant-Accounts-Customer-and-Factor-Analysis/blob/main/images/image.png)

## Data Collection.
We collected data throuh online surveys. there are total 37 features with 1092 observations.

## Exploratory Data Aalysis!
* Our output varable is 'Current_status'
* Here are some of the plots involving our output variable and other independent variables
![](https://github.com/maaz97py/Predicting-Dormant-Accounts-Customer-and-Factor-Analysis/blob/main/images2/image.png)

* Heatmap
![](https://github.com/maaz97py/Predicting-Dormant-Accounts-Customer-and-Factor-Analysis/blob/main/images3/image.png)
* all the values less than .5 are not related

## Feature Engineering
* Dropped Features based on Hypothesis Testing(Recursive Feature Elimination and Anova Test)
* Selected features are:
Age,Gender,Education,Occupation,Account Type,Having Min Balance,Multiple Accounts,Active Loan,Internet/Mobile Banking,Credit Card,Whether defaulted Loan,Customer Service Satisfaction,Transaction done in 24 month,Opening Balance,Current Balance,Distance from Bank,Quarterly Activity Rate(no of transactions in 3 month),Current Status of your accounts [Active, Dormant, Inactive] - Output Variable .

## Model Building.
* We tried different models using a library called 'Lazyclassifier'
* and we also tried manually
* Here are the results
* ![](https://github.com/maaz97py/Predicting-Dormant-Accounts-Customer-and-Factor-Analysis/blob/main/images%204/image.png) 
* We selected 'Random Forest' as it gave the best F1 score.

## Deployment 
* We did our model deployment using Flask API.
* ![]()
