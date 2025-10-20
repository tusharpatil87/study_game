import streamlit as st

# Language toggle
language = st.radio("Select Language / भाषा निवडा", ["English", "Marathi"])

# Quiz data (English and Marathi versions)
quiz_data = {
    "English": [
        {
            "question": "What does the poet mean by 'a bower quiet for us'?",
            "options": ["A place full of flowers", "A dark cave", "A noisy forest", "A peaceful resting place"],
            "answer": 3,
            "explanation": "The phrase refers to a peaceful and quiet place where one can rest and find solace."
        },
        # Add more questions here...
    ],
    "Marathi": [
        {
            "question": "'a bower quiet for us' या ओळीचा अर्थ काय?",
            "options": ["फुलांनी भरलेली जागा", "अंधाराची गुहा", "गोंगाट करणारा जंगल", "शांत विश्रांतीची जागा"],
            "answer": 3,
            "explanation": "ही ओळ शांत आणि विश्रांतीसाठी योग्य जागेचा उल्लेख करते."
        },
        # Add more questions here...
    ]
}

quiz = quiz_data[language]
score = 0

st.title("🌿 A Thing of Beauty - Quiz")
st.progress(0)

for i, q in enumerate(quiz):
    st.subheader(f"Question {i+1}")
    user_answer = st.radio(q["question"], q["options"], key=i)
    if st.button(f"Submit Answer {i+1}", key=f"submit_{i}"):
        if q["options"].index(user_answer) == q["answer"]:
            st.success("✅ बरोबर! / Correct!")
            score += 1
        else:
            st.error("❌ चूक / Incorrect.")
        st.info(f"ℹ️ {q['explanation']}")
        st.progress((i+1)/len(quiz))

# Final score
if st.button("Show Final Score"):
    st.write(f"🎯 Your final score: **{score} / {len(quiz)}**")
    if score == len(quiz):
        st.balloons()
        st.success("🏆 Excellent! You mastered the poem!")
    elif score > len(quiz)//2:
        st.info("👍 Good job! Keep practicing.")
    else:
        st.warning("📘 Review the poem again and try once more.")
