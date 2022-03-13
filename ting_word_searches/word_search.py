def dict_word(path_file, word, occurrences):
    word_in_dict = {
        "palavra": word,
        "arquivo": path_file,
        "ocorrencias": occurrences
    }
    return word_in_dict


def search_by_file(file, word):
    ocurrences = []
    for index, data in enumerate(file['linhas_do_arquivo']):
        if word in data:
            dict_line = {
                "linha": index + 1,
            }
            ocurrences.append(dict_line)
    data = dict_word(
        file['nome_do_arquivo'], word, ocurrences)
    return data


def exists_word(word, instance):
    exists_word = []
    current_queue = instance.queue
    for data in current_queue:
        file = search_by_file(data, word)
        if len(file['ocorrencias']) != 0:
            exists_word.append(file)
    return exists_word


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
