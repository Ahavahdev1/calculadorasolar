from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        consumo = float(request.form['consumo'])
        potencia_painel = float(request.form['potencia_painel'])
        perda_sistema = float(request.form['perda_sistema']) / 100
        irradiacao_media = float(request.form['irradiacao_media'])
        altura_painel = float(request.form['altura_painel'])
        largura_painel = float(request.form['largura_painel'])
        
        # Cálculo da energia produzida por painel por dia
        energia_diaria = potencia_painel * irradiacao_media * (1 - perda_sistema)
        
        # Cálculo da energia produzida por painel por mês
        energia_mensal = energia_diaria * 30
        
        # Número de painéis necessários
        num_paineis = consumo / energia_mensal
        
        # Arredondar para cima
        num_paineis = round(num_paineis)
        
        # Cálculo da área necessária para instalação
        area_total = num_paineis * (altura_painel * largura_painel)
        
        return render_template('result.html', num_paineis=num_paineis, area_total=area_total)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
