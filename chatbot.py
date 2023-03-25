import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thanks for asking.", "I'm fine, how are you?", "I'm good, thanks!"],
    "what's up": ["Not much, how about you?", "Just hanging out. You?", "Same old, same old."],
    "what are you doing": ["Just chatting with you!", "Answering your questions.", "Helping you out."],
    "good morning": ["Good morning to you too!", "Morning! How are you today?", "Rise and shine!"],
    "good afternoon": ["Good afternoon!", "Hey there! How's your day going?", "Afternoon, how can I help you?"],
    "good evening": ["Good evening!", "Hey there! How's your night going?", "Evening! What's on your mind?"],
    "bye": ["Goodbye!", "See you later!", "Bye for now!"],
    "thanks": ["You're welcome!", "No problem!", "My pleasure!"],
    "help": ["How can I help you?", "What do you need help with?", "I'm here to assist you!"],
    "what is your name": ["My name is Chatbot.", "You can call me Chatbot.", "I'm Chatbot!"],
    "who created you": ["I was created by a team of developers.", "My creators prefer to remain anonymous.", "I was programmed by some really smart people!"],
    "what do you do": ["I'm here to chat with you!", "I can answer your questions.", "I'm a chatbot, so I don't do much besides chat."],
    "what are your hobbies": ["I'm a chatbot, so I don't have hobbies!", "I like talking to people.", "I enjoy answering questions."],
    "what is your favorite color": ["I don't have a favorite color, I'm a chatbot!", "I don't see colors, I'm just lines of code.", "I don't have personal preferences, I'm here to assist you!"],
    "how old are you": ["I don't have an age, I'm a chatbot!", "I was just created recently.", "I don't age like humans do."],
    "what is the meaning of life": ["That's a philosophical question that humans have been pondering for centuries.", "The meaning of life is subjective and varies from person to person.", "I'm not sure I can answer that, but I'm happy to chat about it!"],
    "tell me a joke": ["Why did the tomato turn red? Because it saw the salad dressing!", "Why did the chicken cross the playground? To get to the other slide!", "Why was the math book sad? Because it had too many problems."],
    "what is the weather like": ["I'm sorry, I don't have access to real-time weather information.", "You can check the weather online or on your phone.", "I'm not sure, but I hope it's nice wherever you are!"],
    "what is your favorite food": ["I don't have a favorite food, I'm a chatbot!", "I don't eat, I'm just lines of code.", "I don't have personal preferences, I'm here to assist you!"],
    "what is the capital of France": ["The capital of France is Paris.", "Paris is the capital city of France.", "It's Paris!"],
    "what is the largest country in the world": ["The largest country in the world is Russia.", "Russia is the biggest country by land area"],
    "yes": ["Great!", "Excellent!", "Wonderful!"],
    "no": ["Sorry to hear that.", "That's too bad.", "Hope things get better!"],
    "maybe": ["Hmm, not sure.", "Can you tell me more?", "Let's think about it some more."],
    "sorry": ["It's okay, no worries.", "No problem, everyone makes mistakes.", "Apology accepted!"],
    "cool": ["Glad you think so!", "Awesome!", "Coolio!"],
    "nice": ["Thanks!", "Glad you like it!", "Appreciate it!"],
    "awesome": ["You're awesome too!", "Thanks!", "Rock on!"],
    "fun": ["Sounds like a blast!", "Glad you're having fun!", "Fun is the best!"],
    "interesting": ["Tell me more!", "Fascinating!", "That's really intriguing!"],
    "boring": ["Sorry to hear that.", "That's too bad.", "Maybe we can find something more exciting to talk about!"],
    "love": ["I love you too!", "You're the best!", "Aww, shucks!"],
    "hate": ["Sorry to hear that.", "That's too bad.", "Let's focus on the positive!"],
    "friend": ["Friends are the best!", "Glad we're friends!", "You're a great friend!"],
    "family": ["Family is so important!", "Glad you have a close family!", "Family is forever!"],
    "work": ["Work can be tough sometimes.", "Hope work is going well for you.", "Let's take a break from work and chat!"],
    "school": ["School can be challenging.", "How's school going for you?", "Learning is so important!"],
    "food": ["I love food!", "What's your favorite food?", "Food is life!"],
    "music": ["Music is the best!", "What's your favorite song?", "Let's rock out!"],
    "movie": ["I love movies!", "What's your favorite movie?", "Movie night sounds like a plan!"],
    "book": ["I love to read"]
    }                                             

def respond(user_input):
    user_input = user_input.strip().lower()

    for key in responses:
        if user_input == key:
            return random.choice(responses[key])

    return "I'm sorry, I don't understand. Can you try again?"

print("Welcome to the chatbot! Type 'bye' to exit.")
while True:
    user_input = input("You: ")

    if user_input == "bye":
        print("Chatbot:", respond(user_input))
        break

    print("Chatbot:", respond(user_input))
