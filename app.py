from flask import Flask,request,render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline
from src.pipeline.training_pipeline import initiate_training

application=Flask(__name__)

app=application



@app.route('/')
def home_page():
    return render_template('index.html')

@app.route("/train")
def train():
    initiate_training()
    return jsonify("training completed")


@app.route('/predict', methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    else:
        data=CustomData(
            sex=int(request.form.get('sex')),
            education = int(request.form.get('education')),
            marriage = int(request.form.get('marriage')),
            age = int(request.form.get('age')),
            limit_bal = float(request.form.get('limit_bal')),
            pay_1 = int(request.form.get('pay_1')),
            pay_2 = int(request.form.get('pay_2')),
            pay_3 = int(request.form.get('pay_3')),
            pay_4 = int(request.form.get('pay_4')),
            pay_5 = int(request.form.get('pay_5')),
            pay_6 = int(request.form.get('pay_6')),
            bill_amt1 = float(request.form.get('bill_amt1')),
            bill_amt2 = float(request.form.get('bill_amt2')),
            bill_amt3 = float(request.form.get('bill_amt3')),
            bill_amt4 = float(request.form.get('bill_amt4')),
            bill_amt5 = float(request.form.get('bill_amt5')),
            bill_amt6 = float(request.form.get('bill_amt6')),
            pay_amt1 = float(request.form.get('pay_amt1')),
            pay_amt2 = float(request.form.get('pay_amt2')),
            pay_amt3 = float(request.form.get('pay_amt3')),
            pay_amt4 = float(request.form.get('pay_amt4')),
            pay_amt5 = float(request.form.get('pay_amt5')),
            pay_amt6 = float(request.form.get('pay_amt6')),
        )
        
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)
        
        print("Prediction Value:",pred)
        
        results = ""
        if pred == 1:
            results = "The credit card holder will be Defaulter in the next month"
        else:
            results = "The Credit card holder will not be Defaulter in the next month"

        return render_template('results.html', final_result = results)

        






if __name__ =="__main__":
    app.run(host='0.0.0.0',debug=True)