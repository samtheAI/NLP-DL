# IMDb Sentiment Classification with Deep Learning

An instructor-led, end-to-end NLP project that classifies IMDb movie reviews as positive or negative using a neural network.

## Dataset

Download the [IMDb Dataset of 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews), extract `IMDB Dataset.csv`, and place it at:

```text
data/IMDB Dataset.csv
```

## Project workflow

1. Open `sentiment_dl_training.ipynb`.
2. Run all cells to explore the data, train the model, and evaluate it.
3. The notebook saves the trained model to `artifacts/sentiment_dl.keras`.
4. Start the application:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The saved model includes its `TextVectorization` layer, so `app.py` can send raw review text directly to the model.

## Deployment

Commit `artifacts/sentiment_dl.keras` after training, then deploy `app.py` through Streamlit Community Cloud.
