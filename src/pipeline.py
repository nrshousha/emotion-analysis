from transformers import pipeline

def load_model():
    pipe = pipeline("text-classification",
                    model="j-hartmann/emotion-english-distilroberta-base",
                    top_k=None,
                    model_kwargs={"local_files_only": True}
                    )
    return pipe

def detect_emotion(text, pipe):
    results = pipe(text)[0]  # [0] gets first item from outer list
    results = sorted(results, key=lambda x: x['score'], reverse=True)
    return results
