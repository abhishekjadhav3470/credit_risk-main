import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd


class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        


class CustomData:
    def __init__(self,
                 sex:str,
                 education:str,
                 marriage:str,
                 age:int,
                 limit_bal:float,
                 pay_1:int,
                 pay_2:int,
                 pay_3:int,
                 pay_4:int,
                 pay_5:int,
                 pay_6:int,
                 bill_amt1:float,
                 bill_amt2:float,
                 bill_amt3:float,
                 bill_amt4:float,
                 bill_amt5:float,
                 bill_amt6:float,
                 pay_amt1:float,
                 pay_amt2:float,
                 pay_amt3:float,
                 pay_amt4:float,
                 pay_amt5:float,
                 pay_amt6:float):
        
        self.sex=sex
        self.education=education
        self.marriage=marriage
        self.age=age
        self.limit_bal=limit_bal
        self.pay_1=pay_1
        self.pay_2=pay_2
        self.pay_3=pay_3
        self.pay_4=pay_4
        self.pay_5=pay_5
        self.pay_6=pay_6
        self.bill_amt1=bill_amt1
        self.bill_amt2=bill_amt2
        self.bill_amt3=bill_amt3
        self.bill_amt4=bill_amt4
        self.bill_amt5=bill_amt5
        self.bill_amt6=bill_amt6
        self.pay_amt1=pay_amt1
        self.pay_amt2=pay_amt2
        self.pay_amt3=pay_amt3
        self.pay_amt4=pay_amt4
        self.pay_amt5=pay_amt5
        self.pay_amt6=pay_amt6
        
        
        

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'Sex':[self.sex],
                'Education':[self.education],
                'Marriage':[self.marriage],
                'Age':[self.age],
                'Limit_Bal':[self.limit_bal],
                'Pay_1':[self.pay_1],
                'Pay_2':[self.pay_2],
                'Pay_3':[self.pay_3],
                'Pay_4':[self.pay_4],
                'Pay_5':[self.pay_5],
                'Pay_6':[self.pay_6],
                'Bill_Amt1':[self.bill_amt1],
                'Bill_Amt2':[self.bill_amt2],
                'Bill_Amt3':[self.bill_amt3],
                'Bill_Amt4':[self.bill_amt4],
                'Bill_Amt5':[self.bill_amt5],
                'Bill_Amt6':[self.bill_amt6],
                'Pay_Amt1':[self.pay_amt1],
                'Pay_Amt2':[self.pay_amt2],
                'Pay_Amt3':[self.pay_amt3],
                'Pay_Amt4':[self.pay_amt4],
                'Pay_Amt5':[self.pay_amt5],
                'Pay_Amt6':[self.pay_amt6]
                
                
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)