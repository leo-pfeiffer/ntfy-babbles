import openai
import time
import os
import random
from dotenv import load_dotenv
import requests

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

MONTH_IN_SECONDS = 60 * 60 * 24 * 30

PROMPTS = (
    "Write a cute message for my wife:",
    "Compose an encouraging message for my wife:",
    "Send a loving message to brighten my wife's day:",
)
ADJECTIVES = ("sweet", "gorgeous", "beautiful", "brilliant")
NAMES = ("wife", "angel", "babbles", "rainbow princess dream rat", "baby")

generated_messages = {}

messages = [
    "A beautiful dayt, my love! Remember, you're the sunshine in my life.",
    "You make every day brighter with your smile. Have a wonderful day!",
    "You're the reason behind my smile. I love you more each day.",
    "You're my rock and my inspiration. Keep being amazing!",
    "Sending you a virtual hug to brighten your day. I love you!",
    "You're my favorite person in the world. Thanks for being you.",
    "Just a reminder: You're extraordinary, and I'm lucky to have you.",
    "Don't forget how amazing you are. Keep shining, my love.",
    "Every day with you is a gift. I cherish our time together.",
    "You're the love of my life, and I'm grateful for you every day.",
    "Life with you is an adventure. Let's make today incredible!",
    "I believe in you, and I'm here to support you always.",
    "You're my heart's desire, and I'm thinking of you today.",
    "Just a little reminder: You're loved, you're cherished, and you're amazing.",
    "No matter what, I'm here for you. You're never alone.",
    "You light up my life, and I can't wait to see you later.",
    "Every moment with you is a treasure. Have a fantastic day!",
    "I'm so proud of everything you do. Keep chasing your dreams.",
    "You make my world colorful. Sending you all my love.",
    "Just a quick note to say, 'I love you more than words can express.'",
    "Your smile warms my heart every day. Have a fantastic morning, my love!",
    "In the story of my life, you're the most beautiful chapter. 💖",
    "You're the melody to my song, the color to my world. Shine on!",
    "Wishing you a day as lovely as your presence in my life. 😊",
    "Every moment with you feels like a dream come true. I adore you.",
    "Your love is the fuel that powers my day. Keep being amazing!",
    "You make the ordinary extraordinary. Thank you for being you.",
    "A day with you is a day well spent. Sending you all my love.",
    "My love for you grows stronger with each passing day. 💕",
    "No matter what happens today, remember I'm always by your side.",
    "Life with you is an adventure worth taking. Let's make today special!",
    "You light up my world like no one else. Shine bright, my love!",
    "You are my sunshine on even the cloudiest of days. 😊",
    "You're the reason I smile when I wake up. Have a wonderful day!",
    "You're not just my wife; you're my greatest blessing.",
    "I believe in you more than you can imagine. Go and conquer the day!",
    "Our love story is my favorite. Wishing you a beautiful day ahead.",
    "With you, every day feels like Valentine's Day. I love you endlessly.",
    "You're the missing piece to my puzzle. Thanks for completing me.",
    "Sending you a virtual kiss to start your day. 😘",
    "You're my daily dose of happiness. Keep spreading joy!",
    "Your love is the magic that turns ordinary days into extraordinary ones.",
    "Just a reminder: You are loved, cherished, and adored.",
    "The world is a better place with you in it. Have an amazing day!",
    "Your love is my anchor in the stormy sea of life. Thank you.",
    "You're not just my wife; you're my best friend. Love you always.",
    "I can't imagine my life without you. You complete me in every way.",
    "No matter where life takes us, my heart is always with you.",
    "Your love is the sunshine that brightens my darkest days.",
    "I love you more than words can express. Have a magical day!",
    "You're the reason I believe in happily ever after. 😊",
    "Your presence in my life is a gift I cherish every day.",
    "Your love is the most beautiful song in my heart. Sing on!",
    "You're my forever and always. Sending you all my love today.",
    "With you, every day is Valentine's Day. I love you endlessly.",
    "Your smile is my favorite sight in the world. Keep shining!",
    "My love for you knows no bounds. Have a wonderful day!",
    "You're my heart's desire, and I'm thinking of you today.",
    "You are my everything. Thank you for being in my life.",
    "Just a quick note to say, 'I love you more each day.'"
]

def generate_message(prompt):
    while True:
        # response = openai.Completion.create(
        #     engine="davinci",
        #     prompt=prompt,
        #     max_tokens=50,  # Adjust as needed for desired message length
        #     n=1,  # Number of responses to generate
        #     stop=None,  # Optional stop words to prevent the model from continuing
        #     temperature=0.7  # Adjust for creativity (0.2 for more focused, 1.0 for more random)
        # )
        #new_message = response.choices[0].text.strip()
        
        new_message = random.choice(messages)
        
        current_time = time.time()

        if new_message not in generated_messages:
            generated_messages[new_message] = current_time
            return new_message

        if new_message in generated_messages:
            past_time = generated_messages[new_message]
            if current_time - past_time > MONTH_IN_SECONDS:
                generated_messages[new_message] = current_time
                return new_message


def send_message(message, title):
    requests.post(
        "https://ntfy.sh/my-sweet-babbles", 
        data=message,
        headers={
        "Title": title,
        "Priority": "urgent",
        "Tags": "heart"
        }
    )


def should_send():
    day = datetime.datetime.today().day
    current_hour = datetime.datetime.now().hour
    hour_to_send = (1664525 * day + 1013904223) % 12
    return current_hour == hour_to_send


if __name__ == "__main__":
    if should_send():
        # Randomly select a prompt
        prompt = random.choice(PROMPTS)
        message = generate_message(prompt)
        title = f"To my {random.choice(ADJECTIVES)} {random.choice(NAMES)}"
        send_message(message, title)
