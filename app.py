from flask import Flask, render_template, request, send_file
import numpy as np
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    url = request.form['url']  # O link não será usado, mas pode ser armazenado
    rows, cols = 30, 30
    matrix = np.random.randint(0, 2, (rows, cols))  # Matriz aleatória

    # Criação da imagem em memória
    fig, ax = plt.subplots(figsize=(cols / 10, rows / 10))
    ax.imshow(matrix, cmap='gray', vmin=0, vmax=1)  # Mapeia 0 -> branco e 1 -> preto
    ax.axis('off')  # Remove os eixos

    # Salvar a imagem em um objeto BytesIO
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight', pad_inches=0)
    plt.close(fig)
    img.seek(0)  # Volta ao início do objeto BytesIO

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
