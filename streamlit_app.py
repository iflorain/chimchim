import streamlit as st
import openai
# Uncomment the following lines to enable the API key input form
# Initialize
st.cache_data.clear()

if "openai_api_key" not in st.session_state:
    st.session_state.openai_api_key = ""

openai.api_key = st.session_state.openai_api_key

if "text_error" not in st.session_state:
    st.session_state.text_error = None

if "text" not in st.session_state:
    st.session_state.text = None

if "n_requests" not in st.session_state:
    st.session_state.n_requests = 0

with st.sidebar:
    api_key_form = st.form(key="api_key_form")
    openai_api_key = api_key_form.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    api_key_form_submitted = api_key_form.form_submit_button("Submit")

    if api_key_form_submitted:
        st.session_state.openai_api_key = openai_api_key
        openai.api_key = st.session_state.openai_api_key
        st.success("Your OpenAI API key was saved successfully!")


import pandas as pd

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Function to generate a food recommendation using OpenAI
def generate_food_recommendation(cuisine):
    prompt = f"I want to eat {cuisine} food, what should I choose?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        n=1,
    )
    return response.choices[0].text.strip()

# Streamlit app
def main():
    st.title("Food Recommendation App")

    # User input for the desired cuisine
    cuisine = st.text_input("Enter the cuisine you'd like to eat (e.g., Chinese, Italian, Japanese, etc.):")

    if st.button("Generate Recommendation"):
        if cuisine:
            # Generate recommendation using OpenAI
            recommendation = generate_food_recommendation(cuisine)

            # Create a Pandas DataFrame for the recommendation
            data = {'Cuisine': [cuisine], 'Recommendation': [recommendation]}
            df = pd.DataFrame(data)

            # Display the recommendation in a table
            st.table(df)
        else:
            st.warning("Please enter a cuisine to get a recommendation.")

if __name__ == "__main__":
    main()

