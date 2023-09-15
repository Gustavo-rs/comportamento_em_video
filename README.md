# Comportamento em Video

<div style="text-align:center; display: flex;">
  <img src="https://www.blogs.unicamp.br/socialmente/wp-content/uploads/sites/238/2013/08/games.jpg" alt="Imagem" width="300"></div>

## Bibliotecas usadas

1. cv2: É a biblioteca OpenCV, usada para processamento de imagem e vídeo.
2. numpy as np: Importa a biblioteca NumPy para operações numéricas.
3. time: Importa a biblioteca time para medir o tempo.
4. datetime.timedelta: Importa a classe timedelta da biblioteca datetime para representar o tempo.
s
### Uma mini documentação e uma breve explicação do funcionamento.

`Inicialização da câmera: `
cap = cv2.VideoCapture(2): Inicializa a câmera, especificando que está conectada à porta 2.
Inicialização de variáveis:

`red_time e blue_time: ` Listas para armazenar o tempo em segundos que os objetos vermelhos e azuis passaram em cada quadrante.

`counter: `
Um contador para controlar a frequência de impressões no console.

`Loop principal: `
O loop while True é executado indefinidamente e lê quadros da câmera em cada iteração.
Processamento dos quadros:

Obtém as dimensões do quadro e calcula o ponto central.
Define faixas de cores para vermelho e azul na forma de intervalos HSV.
Cria máscaras para detectar objetos vermelhos e azuis no quadro.
Encontra os contornos de objetos nas máscaras usando cv2.findContours.

`Função get_quadrant:`
Essa função determina em qual quadrante um ponto (x, y) está localizado com base no ponto central do quadro.

`Contagem e cálculo de tempo:`
Para cada contorno detectado em vermelho e azul:
Calcula o quadrante em que o objeto está.
Incrementa a contagem de objetos nesse quadrante.
Incrementa o tempo que os objetos passaram nesse quadrante.
Isso permite contar objetos vermelhos e azuis em cada quadrante e rastrear quanto tempo eles permaneceram lá.

`Desenho de linhas e texto:`
Desenha linhas que dividem o quadro em quatro quadrantes.
Exibe os índices dos quadrantes.

`Exibição do quadro: `
Mostra o quadro com informações sobre os quadrantes, contagens e tempos na janela chamada "Contagem e Tempo por Quadrante".

`Impressão no console: `
A cada 30 frames (ajustável), o programa imprime no console as contagens e os tempos registrados em cada quadrante para objetos vermelhos e azuis.

`Finalização:`
O programa verifica se a tecla 'q' foi pressionada. Se sim, ele encerra o loop principal.
Libera a câmera (cap.release()) e fecha todas as janelas abertas do OpenCV (cv2.destroyAllWindows()).
