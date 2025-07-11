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
    return render_template("home.html")
@app.route("/predict",methods=['POST'])
def predict():
    try:
        input=[]
        for col in train_cols:
            input.append(float(request.form[col]))
        input=[input]
        prediction=model.predict(input)
        prediction="LOAN APPROVED" if prediction==1 else "LOAN NOT APPROVED"
        return render_template("result.html",prediction=prediction)
    except Exception as e:
        return render_template("index.html",error="Fill all inputs")

@app.route("/home")
def predi():
    return render_template("home.html")
@app.route("/index")
def index_page():
    return render_template("index.html")


if __name__=='__main__':
    app.run(debug=True)
