import streamlit as st
from streamlit_monaco import st_monaco
from generate import select_random_problem, generate_hint

st.title("Code Mentor")
with st.sidebar:
    language_option_map = {
        0: "python",
        1: "cpp",
        2: "javascript",
    }
    language_options_pills = st.pills(
        "**Select your programming language**",
        default=0,
        options=language_option_map.keys(),
        format_func=lambda option: language_option_map[option],
        selection_mode="single",
    )
    language = 'python'
    if language_options_pills:
        language = language_option_map[language_options_pills]
    st.markdown(f'Your choosen language is: {language}')
    difficulty_option_map = {
        0: "Novice",
        1: "Intermediate",
        2: "Expert",
    }
    difficulty_options_pills = st.pills(
        "**Select your difficulty level**",
        default=0,
        options=difficulty_option_map.keys(),
        format_func=lambda option: difficulty_option_map[option],
        selection_mode="single",
    )
    difficulty = 'Novice'
    if difficulty_options_pills:
        difficulty = difficulty_option_map[difficulty_options_pills]
    st.markdown(f'Your choosen difficulty is: {difficulty}')

    if st.button('Get Problem', help='Get a random problem based on your selected difficulty level.'):
        problem, solution = select_random_problem(difficulty,language)

content = st_monaco(
    value="",
    height="200px",
    language=language,
    lineNumbers=True,
    minimap=False,
    theme="vs-dark",
)

hint_button = st.button("Get a Hint")

messages = st.container(height=200)
chat_input = st.chat_input("Say something")

if hint_button:
    messages.chat_message("user").write('Give me a hint.')

if prompt := chat_input:
    messages.chat_message("user").write(prompt)
    messages.chat_message("assistant").write(f"Echo: {prompt}")