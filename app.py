import streamlit as st
import json

# Load quiz data from JSON file
with open("data.json", "r", encoding="utf-8") as f:
    quiz_data = json.load(f)

# Language toggle
language = st.radio("Select Subject", list(quiz_data.keys()))

# Topic selection
topic = st.selectbox("Select Topic", list(quiz_data[language].keys()))

# Get the selected quiz
quiz = quiz_data[language][topic]

# Initialize session state for score if it doesn't exist
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.answered = [False] * len(quiz)

# Quiz logic
st.title(f"🌿 {topic} - Quiz")

# Reset score if the quiz changes
if 'current_quiz' not in st.session_state or st.session_state.current_quiz != topic:
    st.session_state.score = 0
    st.session_state.answered = [False] * len(quiz)
    st.session_state.current_quiz = topic

for i, q in enumerate(quiz):
    st.subheader(f"Question {i+1}")
    user_answer = st.radio(q["question"], q["options"], key=f"q_{i}")
    
    # Show feedback for answered questions
    if st.session_state.answered[i]:
        if q["options"].index(user_answer) == q["answer"]:
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect.")
        st.info(f"Explanation: {q['explanation']}")
    
    # Only show submit button if not already answered
    if not st.session_state.answered[i] and st.button(f"Submit Answer {i+1}", key=f"submit_{i}"):
        if q["options"].index(user_answer) == q["answer"]:
            st.session_state.score += 1
        st.session_state.answered[i] = True
        st.rerun()

# Display final score
st.write("---")
st.write(f"Your current score: **{st.session_state.score} / {len(quiz)}**")

# Show completion message if all questions are answered
if all(st.session_state.answered):
    st.balloons()
    st.success(f"🎉 Quiz completed! Final score: {st.session_state.score}/{len(quiz)}")