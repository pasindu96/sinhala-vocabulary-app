import streamlit as st
import numpy as np

arr = np.random.randint(0, 100, 2)
q = f"{arr[0]} * {arr[1]}"
ans = arr[0] * arr[1]
choices = [0, ans, ans - 1, ans + 1, ans + 2]

st.text(f"Solve: {q}")
a = st.selectbox('Answer:', choices)
st.write(f"You chose {a}")

if (ans == int(a)):
    st.write("Correct!")
else:
    st.write(f"Wrong!, the correct answer is {ans}")

st.button('Rerun')