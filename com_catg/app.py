import streamlit as st
import pandas as pd
import pickle
from preprocess import clean_text
import plotly.express as px
from reply_templates import get_reply
from bert_classifier import classify_with_bert
import nltk
from nltk.data import find

def download_if_missing(resource_name, download_name=None):
    try:
        find(f'corpora/{resource_name}')
    except LookupError:
        nltk.download(download_name or resource_name, quiet=True)

# Check and download only if missing
download_if_missing('stopwords')
download_if_missing('wordnet')
download_if_missing('omw-1.4')



# Load model and vectorizer
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Streamlit UI
st.title("🧠 Comment Categorization & Reply Assistant")
st.write("Analyze and classify comments into meaningful categories with reply suggestions.")

# Single comment input
st.subheader("🔍 Analyze a Single Comment")
comment = st.text_area("Enter a comment to categorize")

if st.button("Categorize"):
    if comment.strip() == "":
        st.warning("Please enter a comment.")
    else:
        clean = clean_text(comment)
        vec = vectorizer.transform([clean])
        proba = model.predict_proba(vec)
        confidence = max(proba[0])
        prediction = model.predict(vec)[0]

        # Fallback to BERT if low confidence or uncertain category
        if confidence < 0.6 or prediction in ["Spam", "Question/Suggestion"]:
            prediction = classify_with_bert(comment)

        reply = get_reply(prediction)

        st.success(f"Category: **{prediction}**")
        st.info(f"Suggested Reply: {reply}")

# CSV upload
st.subheader("📂 Analyze Multiple Comments from CSV")
uploaded_file = st.file_uploader("Upload a CSV file with a 'comment' column", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if 'comment' not in df.columns:
        st.error("CSV must contain a 'comment' column.")
    else:
        df['clean'] = df['comment'].astype(str).apply(clean_text)
        vectors = vectorizer.transform(df['clean'])
        df['predicted'] = model.predict(vectors)
        df['reply'] = df['predicted'].apply(get_reply)
        st.write(df[['comment', 'predicted', 'reply']])
        # Show category distribution chart
        st.subheader("📊 Category Distribution")
        category_counts = df['predicted'].value_counts().reset_index()
        category_counts.columns = ['Category', 'Count']

        fig = px.bar(
            category_counts,
            x='Category',
            y='Count',
            color='Category',
            title="Number of Comments per Category",
            text='Count'
        )
        st.plotly_chart(fig)

        csv_out = df.to_csv(index=False)
        st.download_button("Download Results", csv_out, "categorized_comments.csv", "text/csv")
