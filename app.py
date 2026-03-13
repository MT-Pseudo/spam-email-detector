import joblib
from flask import Flask, render_template, request

# load trained model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    probability = ""

    if request.method == "POST":

        email = request.form["email"]

        email_vector = vectorizer.transform([email])

        prediction = model.predict(email_vector)
        probs = model.predict_proba(email_vector)

        spam_prob = round(probs[0][1] * 100, 2)

        if prediction[0] == 1:
            result = "SPAM"
        else:
            result = "NOT SPAM"

        probability = f"{spam_prob}%"

    return render_template(
        "index.html",
        result=result,
        probability=probability
    )


if __name__ == "__main__":
    app.run(debug=True)