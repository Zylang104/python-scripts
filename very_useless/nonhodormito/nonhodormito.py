import cv2
import os

lista_immagini = [
    'guè.jpg',
    'notte1.jpg',
    'notte2.jpg',
    'notte3.jpg',
    'notte4.jpg',
    'notte5.jpg',
    'notte6.jpg',
    'notte7.jpg',
    'notte8.jpg',
    'manoabbiamofumatopoco.jpg',
    'giovanethug.jpg'
]

cartella_immagini = os.path.dirname(__file__)

for file_immagine in lista_immagini:
    percorso_immagine = os.path.join(cartella_immagini, file_immagine)
    img = cv2.imread(percorso_immagine)

    if img is not None:
        cv2.imshow('Presentazione Immagini', img)
        cv2.waitKey(5000)
    else:
        print(f"Errore nel caricamento dell'immagine: {percorso_immagine}")

cv2.waitKey(0)
cv2.destroyAllWindows()