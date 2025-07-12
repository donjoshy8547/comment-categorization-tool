from transformers import pipeline

# Load zero-shot classification pipeline with DistilBERT
classifier = pipeline("zero-shot-classification", model="typeform/distilbert-base-uncased-mnli")

# Define the labels (same as used in training)
labels = [
    "Praise",
    "Support",
    "Constructive Criticism",
    "Hate/Abuse",
    "Threat",
    "Emotional",
    "Spam",
    "Question/Suggestion"
]

def classify_with_bert(text):
    result = classifier(text, candidate_labels=labels)
    return result['labels'][0]  # Return the top predicted label