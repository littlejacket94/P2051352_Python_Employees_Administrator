def calculate_shift_from_id(student_id):
    digits = [int(ch) for ch in student_id if ch.isdigit()]
    return sum(digits)

def encrypt(text, shift):
    encrypted = ""
    for ch in text:
        if ch.isdigit():
            new_digit = (int(ch) + shift) % 10
            encrypted += str(new_digit)
        else:
            encrypted += ch
    return encrypted

def decrypt(text, shift):
    decrypted = ""
    for ch in text:
        if ch.isdigit():
            new_digit = (int(ch) - shift) % 10
            decrypted += str(new_digit)
        else:
            decrypted += ch
    return decrypted
