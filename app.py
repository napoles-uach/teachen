import streamlit as st
import openai
from openai import OpenAI

# OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["gpt_key"]

def openq(prompt_script):
    client = openai.OpenAI(api_key=st.secrets["gpt_key"])
    completion = client.chat_completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Evaluate the following answers to determine the English proficiency level (Beginner, Intermediate, Advanced):\n{prompt_script}\nProvide the overall proficiency level:"}
        ],
        max_tokens=1000
    )
    return completion.choices[0].message['content']

def evaluate_english_level(answers):
    prompt_script = ""
    for idx, answer in enumerate(answers, start=1):
        prompt_script += f"Question {idx}: {answer}\n"
    return openq(prompt_script)

# App title and description
st.title("Learn English with AI")
st.write("This app helps you improve your English skills with personalized AI-driven lessons.")

# Initial Assessment Section
st.header("Initial Assessment")
questions = [
    "Write a sentence using the word 'apple'.",
    "Fill in the blank: He ___ to school every day.",
    "Correct the grammar in this sentence: 'She go to the store yesterday.'",
    "Translate the following sentence to English: 'Elle aime lire des livres.'",
]

user_answers = []
for question in questions:
    answer = st.text_input(question)
    user_answers.append(answer)

if st.button("Submit Answers"):
    if all(user_answers):
        proficiency_level = evaluate_english_level(user_answers)
        st.success(f"Based on your answers, your English proficiency level is: **{proficiency_level}**")

        # Storing the proficiency level in a session state for future use
        st.session_state.proficiency_level = proficiency_level
    else:
        st.error("Please answer all questions before submitting.")

# Learning path section based on proficiency
if 'proficiency_level' in st.session_state:
    st.header(f"Personalized Learning Path for {st.session_state.proficiency_level} Level")
    st.write(f"Here's your learning path based on your assessed English proficiency level of **{st.session_state.proficiency_level}**.")

    if st.session_state.proficiency_level == "Beginner":
        st.subheader("Focus Areas")
        st.write("1. Basic Vocabulary\n2. Simple Grammar Rules\n3. Daily Sentences")
        st.subheader("Today's Challenge")
        st.write("Write three sentences using the word 'book'.")

    elif st.session_state.proficiency_level == "Intermediate":
        st.subheader("Focus Areas")
        st.write("1. Complex Sentence Structures\n2. Verb Tenses\n3. Conversational English")
        st.subheader("Today's Quiz")
        st.write("Which tense is used in this sentence: 'I will be going to the market tomorrow'?")

    elif st.session_state.proficiency_level == "Advanced":
        st.subheader("Focus Areas")
        st.write("1. Advanced Grammar\n2. Writing and Comprehension\n3. Idiomatic Expressions")
        st.subheader("Today's Essay Topic")
        st.write("Discuss the impact of social media on modern communication.")

# Footer
st.write("Keep practicing every day to improve your English skills!")

