from src.pipeline import load_model, detect_emotion
import streamlit as st

pipe = load_model()

# ui
st.title("🎭 Emotion Detector")
st.write("Enter any text and we'll detect the emotions behind it.")

user_input = st.text_area("Your text:", placeholder="Type something here...")

if st.button("Detect emotions"):
    if not user_input:
        st.warning("Please enter some text.")
    else:
        emotions = detect_emotion(user_input, pipe)
        st.subheader("Detected emotions:")
        for emotion in emotions:
            emoji = {'joy': '😊', 'anger': '😠', 'sadness': '😢',
                    'fear': '😨', 'surprise': '😲', 'disgust': '🤢',
                    'neutral': '😐'}.get(emotion['label'], '🎭')
            st.progress(emotion['score'], text= f"{emoji} {emotion['label'].capitalize()}: {emotion['score']*100:.1f}%")