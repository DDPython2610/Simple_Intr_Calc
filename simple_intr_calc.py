import streamlit as st

def calculate_interest(principle, rate, time):
    principle = float(principle)
    rate = float(rate)
    time = float(time)
    interest = principle * rate * time / 100
    return interest

st.title("Simple Interest Calculator")

# Input fields
principle = st.text_input("Principle:")
rate = st.text_input("Interest Rate:")
time = st.text_input("Time Duration:")

# Calculate button
if st.button("Calculate Simple Interest"):
    if principle and rate and time:
        interest = calculate_interest(principle, rate, time)
        st.write(f"Simple Interest: {interest}")
    else:
        st.error("Please fill in all the fields.")