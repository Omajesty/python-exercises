# 8-9. Messages
def show_messages(messages):
    for message in messages:
        print(message)

text_messages = [
    "Hello, how are you?",
    "See you later.",
    "Don't forget your keys.",
]

show_messages(text_messages)

# 8-10. Sending Messages
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

text_messages = [
    "Hello, how are you?",
    "See you later.",
    "Don't forget your keys.",
]
sent_messages = []

send_messages(text_messages, sent_messages)

print("\nOriginal list:")
print(text_messages)
print("Sent messages:")
print(sent_messages)

# 8-11. Archived Messages
text_messages = [
    "Hello, how are you?",
    "See you later.",
    "Don't forget your keys.",
]
sent_messages = []

send_messages(text_messages[:], sent_messages)

print("\nOriginal list:")
print(text_messages)
print("Sent messages:")
print(sent_messages)
