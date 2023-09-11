import sys
import docx


def get_language(char: str):
    alphabet_uk = 'абвгдеєжзиіїйклмнопрстуфхцчшщья'
    alphabet_ru = 'йцукенгшщзхфывапролджэячсмитьбюё'
    alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = ''
    if char.lower() in alphabet_uk:
        alphabet = alphabet_uk
    elif char.lower() in alphabet_ru:
        alphabet = alphabet_ru
    elif char.lower() in alphabet_en:
        alphabet = alphabet_en
    return alphabet


def encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            alphabet = get_language(char.lower())

            index = (alphabet.index(char.lower()) + shift) % len(alphabet)
            if char.islower():
                result += alphabet[index]
            elif char.isupper():
                result += alphabet[index].upper()
        else:
            result += char
    return result


def get_key_caesar():
    while True:
        try:
            encryption_key = int(input("Введіть ключ шифрувння: "))
            return encryption_key
        except Exception:
            print("Введіть число")


def decrypt(text, key_caesar):
    return encrypt(text, -key_caesar)


def create_and_save_docx(file_path, content):
    doc = docx.Document()
    doc.add_paragraph(content)
    doc.save(file_path)


def save_text_to_file(text, output_suffix):
    if len(sys.argv) > 1:
        input_file_name = sys.argv[1]
        file_name, suffix = input_file_name.split('.')

        output_file_name = f"{file_name}{output_suffix}.{suffix}"
        if suffix == 'txt':
            with open(output_file_name, 'w', encoding='utf-8') as output_file:
                output_file.write(text)

        elif suffix == 'doc' or suffix == 'docx':
            create_and_save_docx(output_file_name, text)


def save_encrypted(encrypted_text):
    save_text_to_file(encrypted_text, '_encryp')


def save_decrypted(decrypted_text):
    save_text_to_file(decrypted_text, '_decrypted')


def encrypt_or_decrypt(text, key_caesar):
    while True:
        print("1. Зашифрувти іформацію")
        print("2. Розшифрувти іформацію")
        action = input("Виберіть що потрібно зробити: ")

        print("Результут:")

        if action == '1':
            encrypted = encrypt(text, key_caesar)
            save_encrypted(encrypted)
            print(encrypted)
            break
        elif action == '2':
            decrypted = decrypt(text, key_caesar)
            save_decrypted(decrypted)
            print(decrypted)
            break


def read_docx(file_path):
    doc = docx.Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        suffix = filename.split('.')[1]
        if suffix == 'txt':
            with open(filename) as f:
                text = f.read()
        elif suffix == 'doc' or suffix == 'docx':
            text = read_docx(filename)
    else:
        text = input("Введіть текст: ")

    key_caesar = get_key_caesar()
    encrypt_or_decrypt(text, key_caesar)

    _ = input()


if __name__ == "__main__":
    main()
