import openai

 # Set up the API key for OpenAI
openai.api_key = "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"
# Define the chat history and initial context
chat_history = []
context = ""

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text
    return message.strip()


if __name__ == "__main__":
    # Example usage
    prompt = input("Please add message: ")
    response = generate_response(prompt)
    print(response)