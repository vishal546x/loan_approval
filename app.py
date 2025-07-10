from flask import Flask,request,render_template
import pickle
with open('loan_prediction.pkl','rb')as file:
    model=pickle.load(file)
app=Flask(__name__)
train_cols=['person_income', 'person_home_ownership', 'loan_amnt', 'loan_intent',
       'loan_int_rate', 'loan_percent_income',
       'previous_loan_defaults_on_file']
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict",methods=['POST'])
def predict():
    input=[]
    for col in train_cols:
        input.append(float(request.form[col]))
    input=[input]
    prediction=model.predict(input)
    prediction="yes" if prediction==1 else "No"
    return render_template("index.html",prediction=prediction)

if __name__=='__main__':
    app.run(debug=True)
