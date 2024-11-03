import openai
import os

# Set up OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

def get_ai_response(prompt, language):
    system_message = {
        "role": "system",
        "content": f"You are an AI assistant acting as a multidisciplinary team. Provide answers and support in {language}."
    }
    
    messages = [system_message, {"role": "user", "content": prompt}]
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    return response.choices[0].message["content"].strip()

def main():
    print("Welcome to the AI Q&A Assistant!")
    print("Type 'quit' to exit the program.")
    
    while True:
        language = input("Choose language (English/Arabic): ").lower()
        if language not in ["english", "arabic"]:
            print("Invalid language. Please choose English or Arabic.")
            continue
        
        question = input(f"Enter your question in {language.capitalize()}: ")
        if question.lower() == "quit":
            break
        
        response = get_ai_response(question, language)
        print(f"\nAI Assistant: {response}\n")

if __name__ == "__main__":
    main()
