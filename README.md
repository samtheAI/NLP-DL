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
py -0p
py -3.11 -c "import platform; print(platform.python_version(), platform.architecture()[0])"
py -3.11 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements-windows.txt
streamlit run app.py
```

The version check must print Python `3.11.x` and `64bit`. TensorFlow will not install with 32-bit Python. If `py -3.11` is not found, install the 64-bit Python 3.11 release from [python.org](https://www.python.org/downloads/release/python-3119/), then reopen the terminal.

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
python -m pip install -r requirements-windows.txt
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

### Windows: `No matching distribution found for tensorflow-cpu`

Use the Windows requirements file, which installs the correct TensorFlow package for Windows:

```bat
deactivate
rmdir /s /q .venv
py -3.11 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements-windows.txt
python -c "import tensorflow as tf; print(tf.__version__)"
python -m streamlit run app.py
```

In PowerShell, replace the removal and activation commands with:

```powershell
deactivate
Remove-Item -Recurse -Force .venv
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Do not reuse a virtual environment created with Python 3.8, 32-bit Python, or another unsupported interpreter. Creating a new environment with `py -3.11 -m venv .venv` ensures that `pip` belongs to Python 3.11.

## Deployment

Commit both deployment artifacts after training, then deploy `app.py` through Streamlit Community Cloud using Python 3.11.

Live application: [nlp-dl-sentiment.streamlit.app](https://nlp-dl-sentiment.streamlit.app/)
