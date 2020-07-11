def subsequence(seq):
    if not seq:
        return seq

    M = [None] * len(seq)    # offset by 1 (j -> j-1)
    P = [None] * len(seq)

    # M es una lista. M [j-1] apuntará a un índice de seq que contiene el valor más pequeño 
    #   que podría usarse (al final) para construir una subsecuencia creciente de longitud j.
    # P es una lista. P [i] apuntará a M [j], donde i es el índice de seq. En pocas palabras,
    #   indica cuál es el elemento anterior de la subsecuencia. P se utiliza para construir el resultado al final.



    # Como tenemos al menos un elemento en nuestra lista, podemos comenzar
    # sabiendo que hay al menos una subsecuencia creciente de longitud uno: el primer elemento
    #  L es un número: se actualiza mientras recorre la secuencia y marca la longitud de la subsecuencia más larga
    L = 1
    M[0] = 0

    # Recorriendo la secuencia a partir del segundo elemento
    for i in range(1, len(seq)):
        # Búsqueda binaria: queremos la mayor j <= L
        #  tal que seq [M [j]] <seq [i] (por defecto j = 0),
        #  por lo tanto, queremos el límite inferior al final del proceso de búsqueda.
        lower = 0
        upper = L

        # Dado que la búsqueda binaria no verá el valor del límite superior,
        # tendremos que verificarlo manualmente
        if seq[M[upper-1]] < seq[i]:
            j = upper

        else:
            # bucle de búsqueda binaria real
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seq[M[mid-1]] < seq[i]:
                    lower = mid
                else:
                    upper = mid

            j = lower    #  esto también establecerá el valor predeterminado en 0

        P[i] = M[j-1]

        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
            L = max(L, j+1)

    # Creación del resultado: [seq [M [L-1]], seq [P [M [L-1]]], seq [P [P [M [L-1]]]]], ...]
    result = []
    pos = M[L-1]
    for _ in range(L):
        result.append(seq[pos])
        pos = P[pos]

    return result[::-1]    # invertir 