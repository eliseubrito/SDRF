import cv2

def capturar_fotos():
    # Abrir a câmera
    cam = cv2.VideoCapture(0)

    # Verificar se a câmera foi aberta com sucesso
    if not cam.isOpened():
        print("Erro: Não foi possível abrir a câmera.")
        return

    cv2.namedWindow("Capturar Fotos")

    contador_img = 0

    while True:
        # Capturar frame por frame
        ret, frame = cam.read()

        # Verificar se o frame foi capturado com sucesso
        if not ret:
            print("Falha ao capturar o frame")
            break

        # Exibir o frame
        cv2.imshow("Capturar Fotos", frame)

        # Aguardar pressionamento de tecla
        k = cv2.waitKey(1)

        # Verificar se a tecla ESC (27) foi pressionada para sair
        if k == 27:
            print("Tecla ESC pressionada, encerrando...")
            break

        # Verificar se a tecla SPACE (32) foi pressionada para capturar uma foto
        elif k == 32:
            nome_img = "./images/opencv_frame_{}.jpg".format(contador_img)
            cv2.imwrite(nome_img, frame)
            print("{} gravada!".format(nome_img))
            contador_img += 1

    # Liberar a câmera
    cam.release()

    # Fechar todas as janelas do OpenCV
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capturar_fotos()
