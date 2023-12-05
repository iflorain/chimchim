import streamlit as st

# Function to generate a food recommendation using OpenAI
def generate_food_recommendation(cuisine, meal_type, flavor_preferred):
    prompt = f"I feel like having {meal_type} {cuisine} food with a {flavor_preferred} flavor. What dish do you recommend?. and write 3 notes for me why I chose this cuisine for this {meal_type}."

    # Call OpenAI API for recommendation
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a cuisine recommendation bot. You will help users find the best dishes for their meal."},
            {"role": "user", "content": f"You will help users find the best dishes and make notes from the context:{prompt}."},
        ]
    )

    return response['choices'][0]['message']['content']

# Streamlit app
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
            cuisine = st.text_input("Cuisine:")
            flavor_preferred = st.text_input("Flavor:")

            # Generate recommendation
            if st.button("Generate Recommendation"):
                if meal_type and cuisine and flavor_preferred:
                    recommendation = generate_food_recommendation(meal_type, cuisine, flavor_preferred)
                    st.success(f"Recommended Dish: {recommendation}")
                else:
                    st.warning("Please fill in all fields.")
        else:
            st.error("Invalid API Key. Please enter the correct API key.")

if __name__ == "__main__":
    main()

