def get_plain_list(list_object, cleaned_list):
    """Lista que retorna un arreglo plano a partir de un
    arreglo anidado.

    Args:
        list_object (list): Representa el objeto lista a aplanar
        cleaned_list (list): Representa el objeto lista en su estado inicial (vacío)
        que contendrá los elementos aplanados a partir del objeto lista anidado

    Returns:
        list: Objeto lista aplanado
    """

    for item in list_object:
        # Verificamos si se trata de un objeto lista (de ser un elemento aninado)
        if isinstance(item, list):
            get_plain_list(item, cleaned_list)
        # Si no se trata de un objeto lista, validamos que sea entero
        elif isinstance(item, int):
            cleaned_list.append(item)
    # Retornamos el objeto lista aplanado
    return cleaned_list


if __name__ == "__main__":
    lista = [1, [2, [3, [4, 5]]]]
    cleaned_list_ = get_plain_list(lista, [])
    
    print("Arreglo original: ", lista)
    print("Arreglo plano: ", cleaned_list_)