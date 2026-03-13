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

# 📜 License

Educational project for learning Machine Learning deployment.
