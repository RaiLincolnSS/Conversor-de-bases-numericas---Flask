from flask import Flask, render_template, request, redirect, url_for, flash, session

def converter_base(numero, base):
    if base == 'binario':
        return bin(numero)[2:]
    elif base == 'octal':
        return oct(numero)[2:]
    elif base == 'hexadecimal':
        return hex(numero)[2:]
    else:
        return 'Base não suportada'


app = Flask(__name__)

@app.route('/')
def criar_bases():

    return render_template('index.html')

@app.route('/converter', methods=['POST'])
def converter():
    numero = int(request.form['numero'])
    base = request.form['base']

    try:
        numero = int(numero)
        resultado = converter_base(numero, base)
        return render_template('index.html', resultado=resultado)
    except ValueError:
        return render_template('index.html', error='Número inválido.')


if __name__ == '__main__':
    app.run(debug=True)