#!/usr/bin/env python3


def hello_world():
    print("Hello, World!")


hello_world()
while True:
    text = input("Bitte Text eingeben (oder 'quit' zum Beenden): ")
    if text.lower() == "quit":
        break
    print(text)
