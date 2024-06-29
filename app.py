import streamlit as st
import openai

# OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["gpt_key"]

def openq(prompt_script):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Answer the following question as accurately as possible, try to help as much as you can with this, but be brief and concise. Use markdown format. {prompt_script}"}
        ],
        max_tokens=1000
    )
    return completion.choices[0].message.content

def evaluate_english_level(answers):
    prompt_script = (
        "Evaluate the following answers to determine the English proficiency level "
        "(Beginner, Intermediate, Advanced):\n"
    )
    for idx, answer in enumerate(answers, start=1):
        prompt_script += f"Question {idx}: {answer}\n"
    
    prompt_script += "\nProvide the overall proficiency level:"

    return openq(prompt_script).strip()

# Title and description
st.title("Learn English with AI")
st.write("This app helps you to improve your English skills with the help of AI. Start with an initial assessment to personalize your learning path.")

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
        st.write(f"Based on your answers, your English proficiency level is: **{proficiency_level}**")

        # Store the proficiency level in a session state
        if 'proficiency_level' not in st.session_state:
            st.session_state.proficiency_level = proficiency_level
    else:
        st.error("Please answer all questions before submitting.")

# Display personalized learning path based on the assessed level
if 'proficiency_level' in st.session_state:
    st.header("Personalized Learning Path")

    proficiency_level = st.session_state.proficiency_level
    st.write(f"Your assessed English proficiency level is: **{proficiency_level}**")

    if proficiency_level == "Beginner":
        st.write("Start with basic vocabulary and grammar exercises.")
        # Add beginner level activities here

    elif proficiency_level == "Intermediate":
        st.write("Focus on improving your grammar and sentence construction.")
        # Add intermediate level activities here

    elif proficiency_level == "Advanced":
        st.write("Engage in advanced reading comprehension and writing practice.")
        # Add advanced level activities here

# Footer
st.write("Keep practicing every day to improve your English!")
