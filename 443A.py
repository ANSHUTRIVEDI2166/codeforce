s = input()

# Remove the curly braces
s = s[1:-1]

if not s.strip():
    print(0)
else:
    letters = s.split(", ")
    unique_letters = set(letters)
    print(len(unique_letters))
