Project Report: Comment Categorization & Reply Assistant Tool

Objective

    The Comment Categorization & Reply Assistant Tool is designed to streamline the process of moderating and responding to user-generated comments on platforms such as social media, product pages, or forums. The tool leverages machine learning and natural language processing to automatically classify comments based on intent and sentiment, and to provide appropriate pre-formulated responses. This empowers brands and creative teams to manage feedback effectively and professionally.

Project Overview

    The tool is a lightweight, efficient, and intelligent application capable of identifying and categorizing user comments into meaningful classes, including Praise, Support, Constructive Criticism, Hate/Abuse, Threat, Emotional, Spam, and Question/Suggestion. It combines a traditional machine learning classifier for speed with a transformer-based fallback model for contextual accuracy.

Development Approach

    The project follows a modular development approach with a well-defined directory structure, allowing for scalable and maintainable code organization. The main development phases are as follows:

1. Dataset Preparation:
    A curated dataset of labeled comments was compiled to represent a wide range of user feedback. The dataset includes at least 100–200 samples and is used for training and testing the model.

2. Preprocessing Pipeline:
    Natural language preprocessing techniques were applied, including text normalization, lemmatization, and stopword removal, to ensure data consistency and improve model accuracy.

3. Model Training:
    A logistic regression classifier was trained using TF-IDF features. This model provides fast and effective initial categorization for most straightforward comments.

4. Transformer-Based Fallback:
    For comments with low confidence predictions or those categorized as "Spam" or "Question/Suggestion", a transformer-based model (DistilBERT or multilingual XLM-RoBERTa) was used for zero-shot classification, enhancing the tool's ability to handle nuanced and multilingual inputs.

5. User Interface:
    A clean, interactive user interface was built using Streamlit. Users can upload CSV files or input individual comments. The tool then displays categorized results along with suggested reply templates.

6. Visualization:
    The tool includes a data visualization component that presents the distribution of categorized comments in an interactive bar chart, providing insights into user sentiment trends.


Key Features

Hybrid ML architecture (Logistic Regression + BERT fallback)

Automated sentiment-based comment classification

Predefined professional reply templates for each category

Interactive visual feedback (category distribution)

Streamlit-based GUI

Offline .exe version for non-technical users

How to Run the Application

Web Interface:

Launch the tool using Streamlit: streamlit run app.py

Offline Executable:

Double-click app.exe from the dist directory to run the app locally

Comment Categories Used:

Praise

Support

Constructive Criticism

Hate/Abuse

Threat

Emotional

Spam

Question/Suggestion

Conclusion

    This tool demonstrates a practical and scalable approach to NLP-based comment management. By combining fast ML predictions with intelligent fallback mechanisms, it provides a balanced trade-off between performance and accuracy. The clear categorization and auto-response system help brands improve engagement and sentiment management efficiently.