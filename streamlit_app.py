import streamlit as st
from streamlit import secrets

openai.api_key = secrets["openai_api_key"]


def generate_cuisine_recommendation(cuisine, meal_type, flavor_preferred):
    # Customize the prompt based on your requirements
    prompt = f"I feel like having {meal_type} {cuisine} food with a {flavor_preferred} flavor. What dish do you recommend?. and write 3 notes for me why I chose this cuisine for this {meal_type}."

    # Call OpenAI API for recommendation
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        top_p=0.7,
        max_tokens=450,
        messages=[
            {"role": "system", "content": "You are a cuisine recommendation bot. You will help users find the best dishes for their meal."},
            {"role": "user", "content": f"You will help users find the best dishes and make notes from the context:{prompt}."},
        ]
    )
    
    return response.choices[0].message.content

#st.title("Dish For Today")
st.markdown("<h2 style = 'font-size: 1.8rem'>Dish For Today</h2>",unsafe_allow_html=True)

# Uncomment the following lines to enable the API key input form

def main():
    st.title("Dish For Today")

    # Ask for OpenAI API key as a password
    api_key = st.text_input("Enter OpenAI API Key:", type="password")

    if st.button("Submit"):
        # Check if the API key is correct (you may want to implement a more secure validation)
        if api_key == "your_secret_api_key":
            st.success("API Key Verified! You have access to the app.")
            # User input
            meal_type = st.text_input("Meal Type:")
            cuisune = st.text_input("Cuisine:")
            flavor_preferred = st.text_input("Flavor:")

# Generate recommendation
            if st.button("Generate Recommendation"):
                if meal_type and cuisune and flavor_preferred:
                    recommendation = generate_cuisine_recommendation(
                    meal_type, cuisune, flavor_preferred
        )
                    st.success(f"Recommended Dish: {recommendation}")
                else:
                    st.warning("Please fill in all fields.")
        else:
            st.error("Invalid API Key. Please enter the correct API key.")
            
if __name__ == "__main__":
    main()