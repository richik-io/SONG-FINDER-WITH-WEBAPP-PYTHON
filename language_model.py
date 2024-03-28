# language_model.py
import openai

# Set your OpenAI API key
openai.api_key = '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'

def generate_response(prompt):
    # Generate response using GPT model
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose other engines based on your needs
        prompt=prompt,
        max_tokens=100  # Adjust max_tokens based on the length of the response you want
    )
    return response.choices[0].text.strip()
