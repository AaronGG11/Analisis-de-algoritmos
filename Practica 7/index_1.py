def recursive_solution(remaining_sequence, bigger_than=0):
    '''
        Encuentra la subsecuencia creciente más larga de la secuencia 
        restante que es mayor bigger_than y la devuelve.
    '''

    # Caso base: la secuencia es vacia                                       
    if len(remaining_sequence) == 0:
        return remaining_sequence

    # Caso recursivo 1: quitar el elemento actual y procesar el resto
    best_sequence = recursive_solution(remaining_sequence[1:], bigger_than) 

    # Caso recursivo 2: incluimos el elemento actual si es lo suficientemente grande.        
    first = remaining_sequence[0]

    if (first > bigger_than) or (bigger_than == 0):
        sequence_with = [first] + recursive_solution(remaining_sequence[1:], first)
        # Elejimos el caso 1 y el caso 2 que fueron más largos                       
        if len(sequence_with) >= len(best_sequence):
            best_sequence = sequence_with

    return best_sequence  
