import struct

def hide_script_in_jpeg_polyglot(image_path, script_path, output_path):
    # Leer la imagen JPEG
    with open(image_path, 'rb') as img_file:
        img_data = img_file.read()

    # Encontrar el marcador de fin de la imagen JPEG (FF D9)
    eof_marker_index = img_data.rfind(b'\xff\xd9')
    if eof_marker_index == -1:
        raise ValueError("No se encontró el marcador EOF en la imagen JPEG.")

    # Leer el script
    with open(script_path, 'rb') as script_file:
        script_data = script_file.read()

    # Crear los datos del archivo políglota
    polyglot_data = img_data[:eof_marker_index + 2] + script_data

    # Escribir el archivo políglota
    with open(output_path, 'wb') as output_file:
        output_file.write(polyglot_data)

# Ejemplo de uso
hide_script_in_jpeg_polyglot('cat.jpg', 'LinEnum.sh', 'poly_test.jpg')
