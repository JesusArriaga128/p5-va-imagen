import cv2 
# Leer la imagen con cv2 = computer vision 
img = cv2.imread('Skylan-R34.jpg')
# Determinar el tipo de imagen numpy.ndarray
print(type(img))
# Mostrar pixeles 
print(img.shape)
# Mostrando imagen en ventana barra de titulo Skylan 0019
cv2.imshow('Skylan 0019', img)
## Tiempo de espera 
cv2.waitKey(0)
# Destruir todas las ventanas 
cv2.destroyAllWindows()