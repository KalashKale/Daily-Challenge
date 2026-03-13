def check_palindrome(sequence):
    sequence = sequence.replace(" ", "").lower()
    return sequence == sequence[::-1]

print(f"Palindrome - {check_palindrome('Was it a car or a cat I saw')}")