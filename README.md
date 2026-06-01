# 🎭 Emotion Detector

A deep learning-powered app that detects emotions in text using a pre-trained transformer model.

## Demo

> *"I can't believe I actually did it — after months of hard work, I finally got accepted into my dream university!"*

<img width="1440" height="900" alt="Screenshot 2026-06-01 at 3 35 51 PM" src="https://github.com/user-attachments/assets/94647333-c641-4413-afa9-b1a85e628b7e" />


## What it does

Enter any text and the app returns a breakdown of 7 emotions with confidence scores visualized as progress bars:

😊 Joy | 😠 Anger | 😢 Sadness | 😨 Fear | 😲 Surprise | 🤢 Disgust | 😐 Neutral

## How it works

1. Text is passed to a pre-trained **DistilRoBERTa** model fine-tuned on emotion classification
2. The model returns confidence scores for all 7 emotions
3. Results are sorted by score and displayed as progress bars in Streamlit

No training required — the model was downloaded from HuggingFace and runs locally.

## Project Structure

```
emotion analysis/
├── emotion_model/            # pre-trained model weights (local)
├── src/
│   └── pipeline.py           # model loading and inference logic
├── app.py                    # Streamlit web interface
└── requirements.txt
```

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Model

**j-hartmann/emotion-english-distilroberta-base**
- Architecture: DistilRoBERTa
- Fine-tuned on: 6 emotion datasets
- Labels: anger, disgust, fear, joy, neutral, sadness, surprise

## Tech Stack

- Python
- HuggingFace Transformers
- PyTorch
- Streamlit
