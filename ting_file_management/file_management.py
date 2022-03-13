import sys


def txt_importer(path_file):
    if path_file.endswith(".txt"):

        try:
            with open(path_file, "r") as file:
                text = file.read()
                return text.split("\n")

        except FileNotFoundError:
            sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    else:
        sys.stderr.write("Formato inválido\n")
