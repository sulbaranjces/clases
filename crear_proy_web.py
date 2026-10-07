

import sys

import os



def pedir_nombre_proyecto():
    nombre = input("Ingrese el nombre: ").strip()
    if not nombre:
        print("el nombre del proyecto no puede estar vacio")
        sys.exit(1)
    return nombre

def crear_estructura(nombre_proyecto):
    print("el proyecto sera: ",nombre_proyecto)
    ruta_base = os.path.join(os.getcwd(),nombre_proyecto)

    if os.path.exists(ruta_base):
        print(f"la carpeta '{nombre_proyecto}' ya existe en {os.getcwd()}")
        sys.exit(1)

    os.makedirs(os.path.join(ruta_base,"img"),exist_ok=False)
    os.makedirs(os.path.join(ruta_base, "styles"), exist_ok=False)
    os.makedirs(os.path.join(ruta_base, "js"), exist_ok=False)

    archivo_css = os.path.join(ruta_base, "styles", "style.css")
    archivo_js = os.path.join(ruta_base, "js", "script.js")
    archivo_html = os.path.join(ruta_base, "index.html")

    with open(archivo_css, "w", encoding="utf-8") as css:
        css.write(
            """body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 2rem;
    background: #f4f4f4;
    color: #222;
}

h1 {
    color: #333;
}
"""
        )

    with open(archivo_js, "w", encoding="utf-8") as js:
        js.write(
            """console.log("Hola mundo desde el proyecto web");
"""
        )

    with open(archivo_html, "w", encoding="utf-8") as html:
        html.write(
            f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{nombre_proyecto}</title>
    <link rel="stylesheet" href="styles/style.css">
</head>
<body>
    <h1>Hola mundo</h1>
    <script src="js/script.js"></script>
</body>
</html>
'''
        )

    print(f"Proyecto '{nombre_proyecto}' creado correctamente en: {ruta_base}")

def main():
    if len(sys.argv) > 1 :
        nombre_proyecto = sys.argv[1].strip()
        if not nombre_proyecto :
            nombre_proyecto = pedir_nombre_proyecto()
    else:
        nombre_proyecto = pedir_nombre_proyecto()
    
    crear_estructura(nombre_proyecto)

if __name__ == "__main__":
    main()
