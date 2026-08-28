import streamlit as st
import calendar

st.title("📅 Calendar Generator")

year = st.number_input(
    "Enter Year",
    min_value=1,
    max_value=9999,
    value=2026,
    step=1
)

month = st.number_input(
    "Enter Month (1-12)",
    min_value=1,
    max_value=12,
    value=10,
    step=1
)

if st.button("Generate Calendar"):
    result = calendar.month(int(year), int(month))
    st.code(result)
