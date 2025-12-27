import os

def print_tree(directory=".", prefix=""):
    """Imprime la estructura de carpetas y archivos de forma jerárquica."""
    try:
        paths = sorted([p for p in os.listdir(directory) if not p.startswith('__') and not p.startswith('.')])
    except PermissionError:
        print(prefix + "└── [Acceso denegado]")
        return

    pointers = ["├── "] * (len(paths) - 1) + ["└── "] if paths else []
    for pointer, path in zip(pointers, paths):
        full_path = os.path.join(directory, path)
        print(prefix + pointer + path)
        if os.path.isdir(full_path):
            extension = "│   " if pointer == "├── " else "    "
            print_tree(full_path, prefix + extension)

print("Estructura actual del proyecto:\n")
print_tree(".")