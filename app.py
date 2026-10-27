import streamlit as st

# Intilialize session state for age if not already set
if "age_number" not in st.session_state:
    st.session_state.age_number = 25
   
def update_from_number():
    st.session_state.age_slider = st.session_state.age_number


def update_from_slider():
    st.session_state.age_number = st.session_state.age_slider


st.title("Personal Detail Page")

name = st.text_input("Enter your name:")

st.number_input("Enter your age:", min_value=0, max_value=100, value=25, key="age_number", on_change=update_from_number)
st.slider("Age (Slider View):", min_value=0, max_value=100, value=25, key="age_slider", on_change=update_from_slider)


mail = st.text_input("Enter your Email:")


agree = st.checkbox("I agree to the terms and conditions.")

clicked = st.button("Submit")


if clicked:
    st.success(f"Hello, {name}! You are {st.session_state.age_number} years old and signed in using is {mail}.")
