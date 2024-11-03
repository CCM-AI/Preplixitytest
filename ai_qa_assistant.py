import random

# Simple knowledge base
knowledge_base = {
    "english": {
        "greetings": ["Hello!", "Hi there!", "Greetings!"],
        "farewell": ["Goodbye!", "See you later!", "Take care!"],
        "unknown": ["I'm not sure about that.", "I don't have that information.", "Could you please rephrase your question?"]
    },
    "arabic": {
        "greetings": ["مرحبا!", "أهلا وسهلا!", "السلام عليكم!"],
        "farewell": ["وداعا!", "إلى اللقاء!", "مع السلامة!"],
        "unknown": ["لست متأكدًا من ذلك.", "ليس لدي هذه المعلومات.", "هل يمكنك إعادة صياغة سؤالك من فضلك؟"]
    }
}

def get_response(question, language):
    question = question.lower()
    if any(greeting in question for greeting in ["hello", "hi", "hey", "مرحبا", "أهلا", "السلام"]):
        return random.choice(knowledge_base[language]["greetings"])
    elif any(farewell in question for farewell in ["goodbye", "bye", "see you", "وداعا", "مع السلامة"]):
        return random.choice(knowledge_base[language]["farewell"])
    else:
        return random.choice(knowledge_base[language]["unknown"])

def main():
    print("Welcome to the Simple AI Q&A Assistant!")
    print("Type 'quit' to exit the program.")
    
    while True:
        language = input("Choose language (English/Arabic): ").lower()
        if language not in ["english", "arabic"]:
            print("Invalid language. Please choose English or Arabic.")
            continue
        
        question = input(f"Enter your question in {language.capitalize()}: ")
        if question.lower() == "quit":
            break
        
        response = get_response(question, language)
        print(f"\nAI Assistant: {response}\n")

if __name__ == "__main__":
    main()
