import streamlit as st
import openai

# OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["gpt_key"]

def openq(prompt_script):
    client = openai
    completion = client.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Answer the following question as accurately as possible, try to help as much as you can with this, but be brief and concise. Use markdown format. {prompt_script} "}
        ],
        max_tokens=1000
    )
    return completion.choices[0].message.content

# Title and description
st.title("Learn English with AI")
st.write("This app helps you to improve your English skills with the help of AI. Choose a category to start learning.")

# Vocabulary Section
st.header("Vocabulary Building")
vocabulary = {
    "Apple": "A fruit that is usually red, green, or yellow.",
    "Book": "A set of written or printed pages, usually bound with a protective cover.",
    "Cat": "A small domesticated carnivorous mammal with soft fur."
}

word = st.selectbox("Choose a word to learn", list(vocabulary.keys()))
st.write(f"**{word}**: {vocabulary[word]}")

# Grammar Section
st.header("Grammar Exercises")
st.write("Fill in the blanks with the correct form of the verb.")

grammar_exercises = {
    "He ___ to school every day.": ["goes", "go", "going"],
    "They ___ playing soccer.": ["are", "is", "am"],
    "I ___ a delicious cake yesterday.": ["baked", "bake", "bakes"]
}

for question, options in grammar_exercises.items():
    answer = st.radio(question, options)
    if st.button(f"Check Answer for: {question}"):
        if answer == options[0]:
            st.success("Correct!")
        else:
            st.error("Try again!")

# Practice Section
st.header("Practice with Example Sentences")
st.write("Write your own sentence and get feedback from AI.")

user_sentence = st.text_area("Your sentence", "")
if user_sentence:
    feedback = openq(f"Provide feedback on the following English sentence: {user_sentence}")
    st.write("Your sentence:")
    st.write(user_sentence)
    st.write("AI Feedback:")
    st.write(feedback)

# Footer
st.write("Keep practicing every day to improve your English!")
