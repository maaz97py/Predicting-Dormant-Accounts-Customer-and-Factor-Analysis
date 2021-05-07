from sklearn.ensemble import RandomForestClassifier
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import jsonify
import requests
import pickle
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
import os
from jinja2 import Template

app = Flask(__name__)
# pip3 install flask-bootstrap
Bootstrap(app)
model = pickle.load(open('model_rf_final.pkl', 'rb'))

standard_to = StandardScaler()


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        
        Age = int(request.form['Age'])
        Opening_balance = float(request.form['opening balance'])
        Current_balance = float(request.form['current balance'])
        Dist_of_residence_from_the_bank = float(request.form['Dist of residence from bank'])
        Quarterly_activity_rate = int(request.form['Quarterly activity rate'])
        Months_since_last_transactions = int(request.form['months_last_trans'])
        Gender = str(request.form['gender'])
        Education = str(request.form['education'])
        Occupation = str(request.form['Occupation'])
        Account_type = str(request.form['acc_type'])
        Have_minimum_balance = str(request.form['min_balance'])
        Have_multiple_accounts = str(request.form['multiple_acc'])
        Own_an_active_loan = str(request.form['active_loan'])
        Use_internet_or_mobile_banking = str(request.form['e_banking'])
        Has_an_active_credit_Card = str(request.form['credit_card'])
        Ever_defaulted_on_a_loan = str(request.form['loan_default'])
        Satisfied_with_bank_service = str(request.form['Satisified'])
        Any_transaction_in_the_past_24_months = str(request.form['trans_24_months'])
        
        
        data = [[Gender, Education, Occupation, Account_type, Have_minimum_balance,	
        Have_multiple_accounts, Own_an_active_loan, Use_internet_or_mobile_banking,	
        Has_an_active_credit_Card, Ever_defaulted_on_a_loan, Satisfied_with_bank_service, Any_transaction_in_the_past_24_months, Age, Opening_balance, Current_balance, Dist_of_residence_from_the_bank, Quarterly_activity_rate, Months_since_last_transactions]]
        
        data = pd.DataFrame(data)
        
        list_of_names = ['Gender', 'Education', 'Occupation', 'Account type', 'Have minimum balance?', 'Have multiple accounts?', 'Own an active loan?', 'Use internet or mobile banking?', 'Has an active credit Card?', 'Ever defaulted on a loan?', 'Satisfied with bank service?', 'Any transaction in the past 24 months', 'Age', 'Opening balance', 'Current balance', 'Dist of residence from the bank', 'Quarterly activity rate', 'Months since last transaction']
        
        data.columns = list_of_names
        
        print(data)
        
        prediction = model.predict(data.iloc[:,:])

        '''
        Gender,	Education, Occupation, Account_type, Have_minimum_balance,	
        Have_multiple_accounts,	Own_an_active_loan,	Use_internet_or_mobile_banking,	
        Has_an_active_credit_Card,	Ever_defaulted_on_a_loan, Satisfied_with_bank_service,	
        Any_transaction_in_the_past_24_months, Age, Opening_balance, Current_balance,	
        Dist_of_residence_from_the_bank, Quarterly_activity_rate, Months_since_last_transaction
        
        
        'Gender', 'Education', 'Occupation', 'Account type', 'Have minimum balance?', 
        'Have multiple accounts?', 'Own an active loan?', 'Use internet or mobile banking?', 
        'Has an active credit Card?', 'Ever defaulted on a loan?', 'Satisfied with bank service?', 
        'Any transaction in the past 24 months', 'Age', 'Opening balance', 'Current balance', 
        'Dist of residence from the bank', 'Quarterly activity rate', 'Months since last transaction'
        
        '''

        
        
        '''
        [Age, opening_balance, current_balance, Dist_of_residence_From_bank, 
                                         Quarterly_activity_rate, months_last_trans, gender, education, 
                                         Occupation, acc_type, min_balance, multiple_acc, active_loan, 
                                         e_banking, credit_card, loan_default, Satisified, trans_24_months
        '''
        #print(prediction)
    return render_template('prediction.html', prediction = prediction)

if __name__ == '__main__':
    app.run(port=5000, debug=True)