import numpy as np
import cv2

############ CONFIGURACIÓN DEL SCRIPT ##############

# Pon la ruta a tu imagen en formato '.JPG' a ser posible
# (aunque el resto de formatos también deberían funcionar)

image = cv2.imread('tu_ruta.jpg', cv2.IMREAD_GRAYSCALE)

############ CONFIGURACIÓN DEL SCRIPT ##############

def generate_key(image_shape):
    """Genera una clave aleatoria del mismo tamaño que la imagen"""

    # Puedes modificar el valor '256' por un número del 0 a 256
    # para aumentar el ruido en la encriptación. Este valor representa el modulo
    # de valores posibles que usar entre el negro y el blanco.
    key = np.random.randint(0, 256, image_shape, dtype=np.uint8)
    return key

def encrypt_image(image, key):
    """Encripta la imagen utilizando la clave."""
    if len(image.shape) != 2:
        raise ValueError("La imagen debe ser en blanco y negro.")
    
    # Encriptar la imagen aplicando la operación XOR entre la imagen y la clave
    encrypted_image = cv2.bitwise_xor(image, key)
    
    return encrypted_image

def decrypt_image(encrypted_image, key):
    decrypted_image = cv2.bitwise_xor(encrypted_image, key)
    
    return decrypted_image


if image is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta.")
else:
    # Generar una clave del mismo tamaño que la imagen
    key = generate_key(image.shape)

    encrypted_image = encrypt_image(image, key)
    decrypted_image = decrypt_image(encrypted_image, key)

    cv2.imwrite('imagen_encriptada.jpg', encrypted_image)
    cv2.imwrite('imagen_desencriptada.jpg', decrypted_image)
