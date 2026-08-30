"""Streamlit app for IMDb sentiment prediction with a deep-learning model."""

import json
from pathlib import Path

import numpy as np
import streamlit as st
import tensorflow as tf


MODEL_PATH = Path(__file__).parent / "artifacts" / "sentiment_dl.keras"
VOCABULARY_PATH = Path(__file__).parent / "artifacts" / "vocabulary.json"


@st.cache_resource
def load_artifacts():
    """Load the vocabulary and trained neural network once."""
    if not MODEL_PATH.exists() or not VOCABULARY_PATH.exists():
        raise FileNotFoundError(
            "Model artifacts not found. Run sentiment_dl_training.ipynb first."
        )
    vocabulary = json.loads(VOCABULARY_PATH.read_text(encoding="utf-8"))
    vectorizer = tf.keras.layers.TextVectorization(
        max_tokens=20_000,
        ngrams=2,
        output_mode="int",
        output_sequence_length=300,
        vocabulary=vocabulary,
    )
    return vectorizer, tf.keras.models.load_model(MODEL_PATH, compile=False)


st.set_page_config(page_title="IMDb DL Sentiment Classifier", page_icon="🎬")
st.title("🎬 IMDb Sentiment Classifier")
st.write("Enter a movie review and let the deep-learning model classify its sentiment.")

review = st.text_area(
    "Movie review",
    height=180,
    placeholder="The acting was excellent and I loved the ending!",
)

if st.button("Predict sentiment", type="primary", use_container_width=True):
    if not review.strip():
        st.warning("Please enter a movie review.")
    else:
        try:
            vectorizer, model = load_artifacts()
            vectorized_review = vectorizer(tf.constant([review.strip()]))
            positive_probability = float(
                np.asarray(
                    model.predict(vectorized_review, verbose=0)
                ).reshape(-1)[0]
            )
            negative_probability = 1.0 - positive_probability

            if positive_probability >= 0.5:
                st.success(
                    f"Positive sentiment — {positive_probability:.1%} confidence"
                )
            else:
                st.error(
                    f"Negative sentiment — {negative_probability:.1%} confidence"
                )

            st.write(
                {
                    "Negative probability": f"{negative_probability:.2%}",
                    "Positive probability": f"{positive_probability:.2%}",
                }
            )
        except FileNotFoundError as error:
            st.error(str(error))

st.caption("Teaching model: TextVectorization + Embedding + Global Average Pooling.")
