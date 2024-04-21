'''
Find the largest among the 3 given numbers(value greater than the other two).
Author: Abel C Dixon
Email: 21f1003350@ds.study.iitm.ac.in
'''
import streamlit as st
def largest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

st.title('Largest of 3 numbers')
st.write('Enter the 3 numbers below:')


first_number = st.number_input('Enter the first number:', value=0)
second_number = st.number_input('Enter the second number:', value=0)
third_number = st.number_input('Enter the third number:', value=0)

if st.button('Find the largest number'):
    result = largest_number(first_number, second_number, third_number)
    st.write(f'The largest number is: {result}')

st.markdown('---')
st.markdown('**Copyright © 2024 Abel C Dixon**')
st.markdown('Email: [21f1003350@ds.study.iitm.ac.in](mailto:21f1003350@ds.study.iitm.ac.in)')