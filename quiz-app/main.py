import streamlit as st
import random
import time  # Added to handle slight delay before rerun

# Set page config
st.set_page_config(page_title="Quiz App", page_icon="🧠", layout="centered")

# Initialize session state variables
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "questions" not in st.session_state:
    st.session_state.questions = random.sample([
       {
        "question": "What is the capital of Pakistan?",
        "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"],
        "answer": "Islamabad",
    },
    {
        "question": "What is the process by which plants make their own food?",
        "options": ["Respiration", "Photosynthesis", "Decomposition", "Fermentation"],
        "answer": "Photosynthesis",
    },
    {
        "question": "Which animal is known as the King of the Jungle?",
        "options": ["Lion", "Elephant", "Tiger", "Bear"],
        "answer": "Lion",
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": [
            "Allama Iqbal",
            "Liaquat Ali Khan",
            "Muhammad Ali Jinnah",
            "Benazir Bhutto",
        ],
        "answer": "Muhammad Ali Jinnah",
    },
    {
        "question": "Which is the national language of Pakistan?",
        "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
        "answer": "Urdu",
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Taka", "Riyal"],
        "answer": "Rupee",
    },
    {
        "question": "Which city is known as the City of Lights in Pakistan?",
        "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"],
        "answer": "Karachi",
    },

    ], 7)
    

# Get current question
question_data = st.session_state.questions[st.session_state.question_index]

# UI Layout
st.title("🧠 QUIZ APPLICATION")
st.progress((st.session_state.question_index + 1) / len(st.session_state.questions))

st.markdown(f"### {question_data['question']}")

selected_option = st.radio("Select an answer:", question_data["options"], key="answer")

if st.button("✅ Submit Answer"):
    if selected_option == question_data["answer"]:
        st.success("🎉 Correct!")
        st.session_state.score += 1
        st.balloons()
    else:
        st.error(f"❌ Incorrect! The correct answer is *{question_data['answer']}*.")

    # Move to next question
    if st.session_state.question_index < len(st.session_state.questions) - 1:
        st.session_state.question_index += 1
    else:
        st.success("🎉 Quiz Completed! Great job!")
        st.balloons()  # Balloons when the quiz is completed
        st.session_state.question_index = 0  # Restart quiz
        st.session_state.score = 0  # Reset score

    # Add a small delay before rerun to allow balloons to be seen
    time.sleep(3)
    st.rerun()

# Score Counter
st.sidebar.title("📊 Quiz Stats")
st.sidebar.write(f"✅ Correct Answers: {st.session_state.score}")
st.sidebar.write(f"📌 Questions Answered: {st.session_state.question_index + 1}/{len(st.session_state.questions)}")