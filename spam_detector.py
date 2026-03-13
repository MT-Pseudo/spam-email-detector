import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
df = pd.read_csv("emails.csv")

print("Dataset Preview:")
print(df.head())

# Features and labels
X = df['text']
y = df['spam']

# Convert text to numbers
vectorizer = TfidfVectorizer(stop_words='english')

X = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

print("\nModel Accuracy:", accuracy_score(y_test, y_pred))

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# ==========================
# EMAIL SPAM TESTER
# ==========================

print("\n--- Email Spam Tester ---")

email = input("Paste email text: ")

email_vector = vectorizer.transform([email])

prediction = model.predict(email_vector)
probability = model.predict_proba(email_vector)

spam_probability = probability[0][1]

if prediction[0] == 1:
    print("\nResult: SPAM")
else:
    print("\nResult: NOT SPAM")

print("Spam Probability:", round(spam_probability * 100, 2), "%")