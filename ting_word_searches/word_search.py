def exists_word(word, instance):
    result = []
    for i in range(len(instance)):
        file_data = instance.search(i)
        occurrences = []

        for line_number, line in enumerate(file_data["linhas_do_arquivo"], 1):
            line_words = line.lower().strip().split()
            if any(
                word.lower() == line_word.strip(",.!?;:")
                for line_word in line_words
            ):
                occurrences.append({"linha": line_number})

        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file_data["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return result


def search_by_word(word, instance):
    result = []
    for i in range(len(instance)):
        file_data = instance.search(i)
        occurrences = []

        for line_number, line in enumerate(file_data["linhas_do_arquivo"], 1):
            if word.lower() in line.lower():
                occurrences.append({
                    "linha": line_number,
                    "conteudo": line.strip()
                })

        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": file_data["nome_do_arquivo"],
                "ocorrencias": occurrences
            })

    return result
