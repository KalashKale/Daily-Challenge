def decode_message(message, shift):
    result = ""
    for ch in message:
        if ch == " ":
            result += " "
        else:
            new_pos = (ord(ch) - ord('a') - shift) % 26
            result += chr(new_pos + ord('a'))

    return result