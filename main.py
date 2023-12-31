import cv2
import numpy as np
import time
from datetime import datetime, timedelta

# Função para imprimir no console e gravar em um arquivo
def print_and_save(text, file):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Obtém o carimbo de data e hora atual
    text_with_timestamp = f"{text} - {timestamp}"  # Adiciona o carimbo de data e hora ao texto
    print(text_with_timestamp)
    file.write(text_with_timestamp + '\n')
    file.flush()  # Certifica-se de que os dados sejam escritos imediatamente

# Inicializa a câmera
url = 'http://172.22.19.51:4747/video'
cap = cv2.VideoCapture(url)

red_time = [0, 0, 0, 0]
blue_time = [0, 0, 0, 0]

counter = 0

# Abre o arquivo para gravação
with open('output.txt', 'w') as f:
    while True:
        ret, frame = cap.read()
        height, width, _ = frame.shape
        mid_x, mid_y = width // 2, height // 2

        red_counts = [0, 0, 0, 0]
        blue_counts = [0, 0, 0, 0]

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0, 120, 70])
        upper_red = np.array([10, 255, 255])
        lower_blue = np.array([90, 50, 50])
        upper_blue = np.array([130, 255, 255])

        mask_red = cv2.inRange(hsv, lower_red, upper_red)
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

        contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        def get_quadrant(x, y):
            if x < mid_x:
                return 0 if y < mid_y else 2
            else:
                return 1 if y < mid_y else 3

        current_time = time.time()

        for contour in contours_red:
            if cv2.contourArea(contour) < 500:
                continue
            x, y, w, h = cv2.boundingRect(contour)
            quad = get_quadrant(x, y)
            red_counts[quad] += 1
            red_time[quad] += 1

        for contour in contours_blue:
            if cv2.contourArea(contour) < 500:
                continue
            x, y, w, h = cv2.boundingRect(contour)
            quad = get_quadrant(x, y)
            blue_counts[quad] += 1
            blue_time[quad] += 1

        cv2.line(frame, (mid_x, 0), (mid_x, height), (255, 255, 255), 2)
        cv2.line(frame, (0, mid_y), (width, mid_y), (255, 255, 255), 2)

        for i in range(4):
            cv2.putText(frame, str(i + 1), (mid_x * (i % 2 + 1) - 20, mid_y * (i // 2 + 1) - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow('Contagem e Tempo por Quadrante', frame)

        counter += 1
        if counter % 90 == 0:
            print_and_save("------", f)
            for i in range(4):
                red_str_time = str(timedelta(seconds=red_time[i]))
                blue_str_time = str(timedelta(seconds=blue_time[i]))
                text = f'Quadrante {i + 1}: Vermelhos: {red_counts[i]} (Tempo: {red_str_time}), Azuis: {blue_counts[i]} (Tempo: {blue_str_time})'
                print_and_save(text, f)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
