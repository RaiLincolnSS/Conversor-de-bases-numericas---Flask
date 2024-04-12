# Conversor de bases numericas com Flask


<img width="400" height="400" src="https://img.icons8.com/color/480/000000/flask.png" alt="flask"/>

```
from flask import Flask, render_template, request
```

- Faz as impportações necessárias.


---

```
def converter_base(numero, base):
    if base == 'binario':
        return bin(numero)[2:]
    elif base == 'octal':
        return oct(numero)[2:]
    elif base == 'hexadecimal':
        return hex(numero)[2:]
    

  ```


A função `converter_base(numero, base)` recebe dois parâmetros: `numero`, que é o número a ser convertido, e `base`, que é a base para a qual o número será convertido. 
- Se `base` for igual a 'binario', a função retorna a representação binária de `numero` convertida para uma string, usando `bin(numero)`. O `[2:]` é usado para remover os dois primeiros caracteres, que representam o prefixo '0b'.
- Se `base` for igual a 'octal', a função retorna a representação octal de `numero` convertida para uma string, usando `oct(numero)`. O `[2:]` é usado novamente para remover os dois primeiros caracteres.
- Se `base` for igual a 'hexadecimal', a função retorna a representação hexadecimal de `numero` convertida para uma string, usando `hex(numero)`. O `[2:]` novamente  é usado para remover os dois primeiros caracteres.

---
```
app = Flask(__name__)

```
- Cria uma instancia do flask

---

```
@app.route('/')
def criar_bases():

    return render_template('index.html')

```

- Cria uma rota para a raiz e renderiza o html index.html que, obrigatoriamente, precisa estar no diretorio templates.

---

```
app.route('/converter', methods=['POST'])
def converter():
    numero = int(request.form['numero'])
    base = request.form['base']

    try:
        numero = int(numero)
        resultado = converter_base(numero, base)
        return render_template('index.html', resultado=resultado)
    except ValueError:
        return render_template('index.html', error='Número inválido.')

```

A função `converter()` é associada à rota '/converter' usando o decorador `@app.route()`. Esta rota aceita apenas requisições do tipo POST.

Dentro da função, primeiro obtemos os dados do formulário enviado através da requisição POST. Extraímos o número a ser convertido e a base para a qual ele deve ser convertido.

Em seguida, tentamos converter o número recebido para um inteiro. Se a conversão for bem-sucedida, chamamos a função `converter_base(numero, base)` para realizar a conversão para a base desejada. O resultado da conversão é armazenado na variável `resultado`.

Se ocorrer um erro durante a conversão (por exemplo, se o usuário inserir um texto ao invés de um número), capturamos a exceção `ValueError` e renderizamos o template 'index.html' passando uma mensagem de erro ('Número inválido.') para ser exibida na página.

Finalmente, retornamos o template 'index.html', passando o resultado da conversão (ou a mensagem de erro, se aplicável) como um parâmetro chamado `resultado`. Esse resultado será exibido na página HTML renderizada.

---

```
if __name__ == '__main__':
    app.run(debug=True)

```

- inicia o servidor Flask e faz com que a aplicação web comece a responder a requisições HTTP.






