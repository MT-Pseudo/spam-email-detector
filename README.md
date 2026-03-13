# 📧 Email Spam Detector

A Machine Learning web application that detects whether an email is **SPAM** or **NOT SPAM** using Natural Language Processing (NLP) and a Logistic Regression classifier.

Users can paste email text into the interface and receive a spam prediction along with a confidence score.

---

# 🌐 Live Website

The project is deployed online using Render:

https://spam-email-detector-zkd7.onrender.com

---

# 📂 Dataset

Dataset used for training:

https://www.kaggle.com/datasets/jackksoncsie/spam-email-dataset

This dataset contains labeled email messages where:

| Label | Meaning        |
| ----- | -------------- |
| 1     | Spam Email     |
| 0     | Not Spam (Ham) |

Columns:

| Column | Description   |
| ------ | ------------- |
| text   | Email content |
| spam   | Spam label    |

---

# 🧠 System Architecture

```text
Email Text
     ↓
Text Preprocessing
     ↓
TF-IDF Vectorization
     ↓
Logistic Regression Model
     ↓
Prediction (Spam / Not Spam)
```

---

# ⚙️ Technologies Used

* Python
* Flask
* Scikit-learn
* TF-IDF
* Logistic Regression
* Joblib
* HTML / CSS
* Git
* GitHub
* Render (deployment)

---

# 📁 Project Structure

```text
spam-email-detector
│
├── app.py
├── train_model.py
├── emails.csv
├── spam_model.pkl
├── vectorizer.pkl
├── requirements.txt
├── Procfile
│
└── templates
     └── index.html
```

---

# 💻 Running the Project Locally (Flask)

## Step 1 — Clone Repository

```bash
git clone https://github.com/MT-Pseudo/spam-email-detector.git
cd spam-email-detector
```

---

## Step 2 — Install Dependencies

Windows:

```bash
pip install -r requirements.txt
```

Linux / macOS:

```bash
pip3 install -r requirements.txt
```

---

## Step 3 — Run Flask Application

```bash
python app.py
```

Flask will start a local server:

```
http://127.0.0.1:5000
```

Open the link in your browser.

---

# 🌍 Running the Project Using Render (Deployment)

The project is deployed using Render.

Steps used for deployment:

### 1. Push project to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```

### 2. Create Render Web Service

1. Open Render dashboard
2. Click **New → Web Service**
3. Connect GitHub repository
4. Select repository

### 3. Configure Render Service

Settings used:

Environment:

```
Python
```

Build Command:

```
pip install -r requirements.txt
```

Start Command:

```
gunicorn app:app
```

### 4. Deploy

Render automatically:

1. Pulls the GitHub repository
2. Installs dependencies
3. Runs the Flask application using Gunicorn

---

# 🚀 Features

* Machine Learning based email spam detection
* Web interface for easy testing
* Confidence score for predictions
* Deployable cloud application
* Interactive UI

---

# 🔮 Future Improvements

* Spam keyword highlighting
* Risk meter visualization
* Larger training datasets
* Deep learning models
* Email subject + body detection

---

# 👨‍💻 Authors

This project was developed by:

* **Mohit Thakur**
* **Nitin Kumar**
* **Kunal Behal**

Computer Science Engineering Students

---

🚨 Spam Examples (should return SPAM)
1
Subject: Congratulations! You have won a free iPhone

Congratulations! You have been selected as the lucky winner of a brand new iPhone.
Click here now to claim your prize before the offer expires.

2
Subject: Limited Time Offer

Earn money from home with no experience required.
Sign up today and start making $3000 per week.
Limited time offer.

3
Subject: Urgent Account Verification

Your account has been compromised.
Please verify your account information immediately to avoid suspension.
Click here to verify your details.

4
Subject: Claim Your Reward

You have won a $5000 reward.
Complete the form and claim your reward now.
Don't miss this opportunity.

5
Subject: Cheap Medication Online

Buy prescription drugs online at 80% discount.
No prescription required.
Order now and save big.

Expected result for most of these:

SPAM
Likely to be spam: 80–99%

✅ Legitimate Email Examples (should return NOT SPAM)

6
Subject: Project Meeting Tomorrow

Hi team,

Just a reminder that we have a project meeting scheduled tomorrow at 10 AM.
Please review the documents shared earlier.

Best regards.

7
Subject: Assignment Submission Reminder

Hello everyone,

This is a reminder that the machine learning assignment is due on Friday.
Please upload your final report before the deadline.

8
Subject: Lunch Tomorrow

Hi Rahul,

Are you free for lunch tomorrow around 1 PM?
Let me know if you would like to meet at the usual place.

9
Subject: Software Update

Dear user,

A new software update is available for your application.
Please install the latest version to improve performance and security.

10
Subject: Weekend Trip Plan

Hey,

We are planning a short trip this weekend.
Let me know if you want to join so we can finalize the travel arrangements.

Expected result:

NOT SPAM
Likely to be spam: 0–20%

---

# 📜 License

Educational project for learning Machine Learning deployment.
