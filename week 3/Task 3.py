to_upper = lambda s: s.upper()
def invert(upper_string):
    print("Reversed string:", upper_string[::-1])
text = input("Enter a string: ")
upper_text = to_upper(text)
print("Uppercase:", upper_text)
invert(upper_text)