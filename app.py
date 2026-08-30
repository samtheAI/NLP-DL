"""Streamlit app for IMDb sentiment prediction with a deep-learning model."""

from pathlib import Path

import numpy as np
import streamlit as st
import tensorflow as tf


MODEL_PATH = Path(__file__).parent / "artifacts" / "sentiment_dl.keras"


@st.cache_resource
def load_model():
    """Load the trained model once for all predictions."""
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Model artifact not found. Run sentiment_dl_training.ipynb first "
            "and save the model to artifacts/sentiment_dl.keras."
        )
    return tf.keras.models.load_model(MODEL_PATH)


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
            model = load_model()
            positive_probability = float(
                np.asarray(
                    model.predict(
                        np.asarray([review.strip()], dtype=object), verbose=0
                    )
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
