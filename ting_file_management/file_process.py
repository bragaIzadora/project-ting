import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for item in instance._items:
        if item['nome_do_arquivo'] == path_file:
            return

    lines = txt_importer(path_file)
    if lines is None:
        return

    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    instance.enqueue(file_info)

    print(file_info)


def remove(instance):
    if not instance._items:
        print("Não há elementos")
    else:
        removed_file = instance.dequeue()
        print(f"Arquivo {removed_file['nome_do_arquivo']}"
              " removido com sucesso")


def file_metadata(instance, position):
    try:
        file_info = instance._items[position]
        print(file_info)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
