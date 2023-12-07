import struct

def hide_script_in_jpeg_polyglot(image_path, script_path, output_path):
    # Leer la imagen JPEG original
    with open(image_path, 'rb') as img_file:
        img_data = bytearray(img_file.read())

    # Leer el script a ocultar
    with open(script_path, 'rb') as script_file:
        script_data = script_file.read()

    # Encuentra el final de la imagen JPEG (marcado por FF D9)
    eof_marker = img_data.rfind(bytes([0xFF, 0xD9]))
    if eof_marker == -1:
        raise ValueError("No se pudo encontrar el marcador EOF en el archivo JPEG.")

    # Insertar el script después del marcador EOF, pero dejando el marcador al final
    polyglot_data = img_data[:eof_marker + 2] + script_data + img_data[eof_marker + 2:]

    # Guardar el archivo políglota
    with open(output_path, 'wb') as output_file:
        output_file.write(polyglot_data)

# Ejemplo de uso
hide_script_in_jpeg_polyglot('cat.jpg', 'LinEnum.sh', 'poly_test.jpg')
