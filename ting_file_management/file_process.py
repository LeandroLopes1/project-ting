from ting_file_management.file_management import txt_importer
import sys


def process_all(path_file):
    text_list = txt_importer(path_file)
    text_list_len = len(text_list)
    line1 = {"nome_do_arquivo": path_file}
    line2 = {"qtd_linhas": text_list_len}
    line3 = {"linhas_do_arquivo": text_list}
    line1.update(line2)
    line1.update(line3)

    return line1


def process(path_file, instance):
    queue = instance.queue
    if path_file in [data['nome_do_arquivo'] for data in queue]:
        return f"Arquivo {path_file} já foi processado"
    else:
        line1 = process_all(path_file)
        instance.enqueue(line1)
        file_string = str(line1)
        sys.stdout.write(file_string)


def remove(instance):
    if len(instance.queue) > 0:
        remove_text = instance.dequeue()
        sys.stdout.write(
            f"Arquivo {remove_text['nome_do_arquivo']} removido com sucesso\n")

    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    try:
        text = instance.search(position)
        sys.stdout.write(str(text))
    except IndexError:
        sys.stderr.write("Posição inválida\n")
