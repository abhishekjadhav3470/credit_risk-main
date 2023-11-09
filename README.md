 #### Life cycle of Machine learning Project
* Understanding the Problem Statement
* Data Collection
* Exploratory data analysis
* Data Pre-Processing
* Model Training
* Model evaluation

## Credit Card Default Prediction
### 1)Project Overview :
* Credit Card Default Prediction is a classification problem.
* Credit Card payment default occurs when you fail to pay the Minimum Amount Due (MAD) on the credit card for a few consecutive months.
* The goal of this project is to predict the probability of credit card default based on credit card owner's characteristics and payment history.
* The dataset contains information on default payments, demographic factors, credit data, history of payment, and bill statements of credit card clients in Taiwan from April 2005 to September 2005.The project understands weather the other independent variables impacts default rate.


### 2)Data Collection
* Dataset Source - https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset
* The data consist of 30000 records and 25 columns

#### 2.1 Data Descriptiion

There are 25 variables:

* ID: ID of each client
* LIMIT_BAL: Amount of given credit in NT dollars (includes individual and family/supplementary credit)
* SEX: Gender (1=male, 2=female)
* EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)
* MARRIAGE: Marital status (1=married, 2=single, 3=others)
* AGE: Age in years
* PAY_0: Repayment status in September, 2005 (-1= pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine months and above)
* PAY_2: Repayment status in August, 2005 (scale same as above)
* PAY_3: Repayment status in July, 2005 (scale same as above)
* PAY_4: Repayment status in June, 2005 (scale same as above)
* PAY_5: Repayment status in May, 2005 (scale same as above)
* PAY_6: Repayment status in April, 2005 (scale same as above)
* BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar)
* BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar)
* BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar)
* BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar)
* BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar)
* BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar)
* PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar)
* PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar)
* PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar)
* PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar)
* PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar)
* PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar)
default.payment.next.month: Default payment (1=yes, 0=no)


Software and Tools Required
* 1.Github account
* 2.AWS Account
* 3.VS code IDE



### Project requirements :
#### Create a virtual environment:
``` 
    conda create -p venv python==3.8 -y
 
    conda activate
```

#### import the required libraries
``` 
    pip install -r requirements.txt

````

#### Github commands:
* git init
* git add README.md
* git commit -m "first commit"
* git branch -M main
* git remote add origin <github path>
* git push -u origin main

#### Best Model is RandomForestClassifier

### Abhishek Jadhav
