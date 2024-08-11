from flask import Flask, render_template, request

app = Flask(__name__)

def normalizeShift(shift):
    return (shift % 26 + 26) % 26

def encrypt(text, shift):
    shift = normalizeShift(shift)
    result = ''
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            encrypted_char = chr(((ord(ch) - base + shift) % 26) + base)
            result += encrypted_char
        else:
            result += ch
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', title='Caesar Cipher')

@app.route('/process', methods=['POST'])
def process():
    text = request.form['text']
    shift = int(request.form['shift'])
    action = request.form['action']
    
    if action == 'encrypt':
        result_text = encrypt(text, shift)
    elif action == 'decrypt':
        result_text = decrypt(text, shift)
    else:
        result_text = 'Invalid action'

    return render_template('index.html', title='Caesar Cipher', result_text=result_text)

if __name__ == '__main__':
    app.run(port=9090)
