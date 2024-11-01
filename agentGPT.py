import openai
import os

# Load the API key
openai.api_key = os.getenv("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")


def query_openai(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",  # Use text-davinci-003 or another model
        prompt=prompt,
        max_tokens=100  # Set the response length, adjust if needed
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    print("Welcome to AgentGPT! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        answer = query_openai(user_input)
        print(f"AgentGPT: {answer}")