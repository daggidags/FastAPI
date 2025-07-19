import joblib
import streamlit as st

st.title("Movie Review Sentiment Classifier")
st.write("Enter a movie review below and the app will predict whether the sentiment is **positive** or **negative**.")

@st.cache_data
def load_model(path='sentiment_model.pkl'):
    model = joblib.load(path)
    return model

model = load_model()

review_text = st.text_area("Enter a movie review to analyze:", height=200)

# Analyze button
if st.button("Analyze"):

    if review_text.strip() == "":
        st.warning("Please enter a review before clicking Analyze.")
    else:
        # Make prediction
        prediction = model.predict([review_text])[0]
        prediction_proba = model.predict_proba([review_text])[0]

        # Display prediction
        if prediction == "positive":
            st.subheader("Predicted Sentiment: Positive 👍")
            st.write(f"Confidence: {prediction_proba[model.classes_.tolist().index('positive')]:.2%}")
        else:
            st.subheader("Predicted Sentiment: Negative 👎")
            st.write(f"Confidence: {prediction_proba[model.classes_.tolist().index('negative')]:.2%}")