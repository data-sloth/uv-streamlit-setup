import streamlit as st
from myproject.pkg2 import complex_fn

def main():
    st.header("Hello from uv-streamlit-setup!")

    val1 = st.number_input('Value 1')
    val2 = st.number_input('Value 2')

    st.write(f"The square of ({val1} - {val2}) is {complex_fn.square_of_diff(val1, val2)}!")


if __name__ == "__main__":
    main()
