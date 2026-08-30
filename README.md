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
4. Start the application using the instructions for your operating system below.

The notebook saves two deployment artifacts:

- `artifacts/sentiment_dl.keras` — the trained neural network
- `artifacts/vocabulary.json` — the vocabulary used to vectorize raw reviews

## Run on Windows

Install Python 3.11 from [python.org](https://www.python.org/downloads/) and select **Add Python to PATH** during installation.

Open Command Prompt in the project folder and run:

```bat
py -3.11 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

For PowerShell, activate the environment with:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, run this once in the same window:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Then start the app:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed in the terminal, usually `http://localhost:8501`.

To stop the app, press `Ctrl+C`. To leave the virtual environment, run:

```bat
deactivate
```

## Run on macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed in the terminal, usually `http://localhost:8501`.

## Troubleshooting

- Run all commands from the repository root—the folder containing `app.py`.
- Use Python 3.11 because the pinned TensorFlow version may not support newer Python versions.
- If `streamlit` is not recognized, activate the virtual environment and run `python -m streamlit run app.py`.
- If the model artifacts are missing, run `sentiment_dl_training.ipynb` from beginning to end.

## Deployment

Commit both deployment artifacts after training, then deploy `app.py` through Streamlit Community Cloud using Python 3.11.

Live application: [nlp-dl-sentiment.streamlit.app](https://nlp-dl-sentiment.streamlit.app/)
