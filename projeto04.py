# Com uso da Biblioteca OPENCV é possível fazer o acesso a camera do dispositivo utilizado, sem a necessidade de fazer um código para acessar as informações dessa camera. Porém devemos lembrar de instala-la, bem como as demais bibliotecas, o que ocorreram diretamente no console Python.

import cv2
from cvzone.HandTrackingModule import HandDetector    # módulo de rastreamento das mãos
webcam = cv2.VideoCapture(0)  # Foi declarado que será capturada as imagens da webcam 0(zero), que por padrão é a camera do dispositivo usado

rastreador = HandDetector(detectionCon=0.8, maxHands=2)
# acima configuramos nosso rastreador onde "detectionCon= 80%"" é a confiança mínima que a biblioteca vai usar para detectar uma mão e "maxHands=2" para detecção de no máximo duas mão 

# como se sabe as cameras de video operam com a captação de uma sequência de imagens, transformando-as em imagem (os frmames), para isso:
while True:
    sucesso, imagem = webcam.read()  # nessa condição o read já irá acessar a webcam do PC, se conseguir captar uma imagem retornará com True
                                     # se confirmado com o True ele vai armazenar essa imagem na varíavel imagem
                                     # se não houver conexão por qualquer problema seá exibida a informação de False, não houve conexão
    coordenadas, imagem_maos = rastreador.findHands(imagem)
# acima o código para detectação das mãos que serão identificadas na nossa camera, que é a varíavel "imagem"

    print(coordenadas)  # com isso serão capturadas as coordenadas das mãos
                                
    cv2.imshow("Projeto 4-IA", imagem)    # declarado que as imagens capturadas irão ser arquivadas e "Projeto 4-IA"
# A fim de evitar que nosso programa de captura de imagens fique capturando infinitamente, com o próximo comando vamos determinar que:
# Ao apertar qualquer tecla do meu teclado ele pare essa captura e arquive no Projeto 4 - IA
    if cv2.waitKeyEx(1) != -1: # esse comando irá monitorar nosso teclado a cada um mile segundo e por padrão ele entende -1 essa sequência de leitura do teclado
        break                # então, quando apertamos qualquer tecla essa sequência de mile segundos -1 é quebrada e da o break

# Posteriormente teremos um código que vai desativar essa condição de acesso a webcam, visto deixa-la a seu estado normal de utilização
webcam.release()
cv2.destroyAllWindows()        # comando para que se encerre todas as janelas

"""
Ainda nos conceitos de Python, temos como biblioteca a mediapipe que trata-se de ma biblioteca que possui recursos
incríveis, como por exemplo o mapeamento das mãos, porém foi desenvolvido uma biblioteca que fortifica o mediapipe e facilita sua usuabilidade que é a biblioteca, cvzone. Portanto para um bom desenvolvimento de qualquer projeto recomenda-se trabalhar com essas duas bibliotecas.
"""




