
# Simple FAQ Chatbot using only Python built-in libraries

# Step 1: FAQs
faqs = {
    "What is Python?": "Python is a high-level, interpreted programming language.",
    "How to install Python?": "You can install Python from python.org or using package managers like apt or brew.",
    "What is a list in Python?": "A list is a collection of items in Python, which is ordered and mutable.",
    "How to define a function in Python?": "You define a function using the 'def' keyword followed by the function name.",
    "What is a chatbot?": "A chatbot is a computer program designed to simulate conversation with human users."
}

# Step 2: Simple preprocessing
def preprocess(text):
    return text.lower().strip()

# Step 3: Find best match using word overlap
def get_answer(user_input):
    user_input = preprocess(user_input)
    max_overlap = 0
    best_answer = "Sorry, I don't know the answer to that."
    
    for question, answer in faqs.items():
        question_processed = preprocess(question)
        # Count common words
        overlap = len(set(user_input.split()) & set(question_processed.split()))
        if overlap > max_overlap:
            max_overlap = overlap
            best_answer = answer
    return best_answer

# Step 4: Chat loop
print("FAQ Chatbot (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_answer(user_input)
    print("Chatbot:", response)