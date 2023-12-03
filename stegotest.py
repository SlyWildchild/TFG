from PIL import Image

filename = 'covered_cat3.png'
filepath =f"C:/Users/Miguel/Documents/UOC/Clase/Asignaturas/TFG/PEC3/{filename}"


# Cargamos la imagen original, asi como sus dimensiones y modo.
orig_image = Image.open(filepath)
width, height = orig_image.size
mode = orig_image.mode

orig_pixel_map = orig_image.load()

# Creamos una nueva imagen que coincide en dimensiones y modo con la original

new_image = Image.new(mode, (width, height))
new_pixel_map = new_image.load()

# Modificamos cada pixel de la nueva imagen
for x in range(width):
    for y in range(height):

        # Descomponemos cada pixel original en sus valores R, G y B
        new_r = new_g = new_b = 0
        orig_pixel = orig_pixel_map[x, y]
        orig_r = orig_pixel[0]
        orig_g = orig_pixel[1]
        orig_b = orig_pixel[2]
        
        # Asignaremos 0 a los valores del nuevo pixel si el pixel original 
        # tiene LSB 1 o 255 si el LSB es 0
        if orig_r %2 == 1: new_r=0
        else: new_r=255
        if orig_g %2 == 1: new_g=0
        else: new_g=255
        if orig_b %2 == 1: new_b=0
        else: new_b=255

        new_pixel = (new_r, new_g, new_b)
        new_pixel_map[x, y] = new_pixel
      
new_image.show()

new_filename = f"modified_{filename}"
new_filepath = f"modified_images/{new_filename}"
new_filepath = f"C:/Users/Miguel/Documents/UOC/Clase/Asignaturas/TFG/PEC3/{new_filename}"
new_image.save(new_filepath)