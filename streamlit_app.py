import streamlit as st

from streamlit_monaco import st_monaco

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

content = st_monaco(
    value="",
    height="200px",
    language=language,
    lineNumbers=True,
    minimap=False,
    theme="vs-dark",
)

if st.button("Get content"):
    st.markdown(f'```{language}\n{content}')