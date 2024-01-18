import streamlit as st

st.write("Hello world")



def main():
    # Set the title of the app
    st.title("String Input App")

    # Get user input for a string
    user_input = st.text_input("Enter a string:")

    # Display the input string
    st.write("You entered:", user_input)

if __name__ == "__main__":
    main()
