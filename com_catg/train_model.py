import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from preprocess import clean_text

# Load and preprocess data
df = pd.read_csv('data/sample_comments.csv')
df.dropna(subset=['comment', 'label'], inplace=True)
df['clean'] = df['comment'].apply(clean_text)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    df['clean'], df['label'], test_size=0.2, random_state=42, stratify=df['label']
)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train Logistic Regression model
model = LogisticRegression(max_iter=1000, multi_class='multinomial', solver='lbfgs')
model.fit(X_train_vec, y_train)

# Evaluate
y_pred = model.predict(X_test_vec)
print("Classification Report:\n")
print(classification_report(y_test, y_pred))

# Save model and vectorizer
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('models/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved in 'models/' folder.")
