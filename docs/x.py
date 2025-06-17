import pyautogui
import random
import time

MIN_DELAY = 4
MAX_DELAY = 6
MIN_TAGS = 1
MAX_TAGS = 3
TYPING_INTERVAL = 0.15

# Common HTML tags and some common attributes
tags = [
    "div", "span", "img", "a", "input", "button", "p", "h1", "h2",
    "ul", "li", "form", "label", "section", "article"
]

attributes = {
    "class": ["container", "header", "footer", "btn", "nav"],
    "id": ["main", "sidebar", "top", "bottom"],
    "src": ["image.jpg", "photo.png", "icon.svg"],
    "href": ["https://example.com", "#home", "#about"],
    "alt": ["An image", "Icon", "Logo"],
    "type": ["text", "submit", "password"],
    "value": ["Submit", "Click", "Enter"],
    "name": ["username", "email", "search"],
    "placeholder": ["Enter text", "Search here"],
}

self_closing = {"img", "input", "br", "hr"}

def generate_tag():
    tag = random.choice(tags)
    attr_string = ""

    # Randomly decide how many attributes to include
    num_attrs = random.randint(0, 2)
    chosen_attrs = random.sample(attributes.items(), k=num_attrs)

    for key, values in chosen_attrs:
        value = random.choice(values)
        attr_string += f' {key}="{value}"'

    if tag in self_closing:
        return f"<{tag}{attr_string}>"
    else:
        return f"<{tag}{attr_string}></{tag}>"

try:
    print("Typing random full HTML tags with clicking. Press Ctrl+C to stop.")
    while True:
        time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))

        num_tags = random.randint(MIN_TAGS, MAX_TAGS)
        html_snippet = '\n'.join(generate_tag() for _ in range(num_tags))

        pyautogui.write(html_snippet, interval=TYPING_INTERVAL)
        pyautogui.press("enter")
        pyautogui.click()
except KeyboardInterrupt:
    print("\nStopped by user.")
