print("=== Word Counter ===")

text = input("Enter your text: ")

words = len(text.split())
characters = len(text)
characters_no_spaces = len(text.replace(" ", ""))
spaces = text.count(" ")
sentences = text.count(".") + text.count("!") + text.count("?")

print("\n==== Result ====")

print("Words:", words)
print("Characters:", characters)
print("Characters (without spaces):", characters_no_spaces)
print("Spaces:", spaces)
print("Sentences:", sentences)