import time
import numpy as np
def compress(file_path):
    start_time = time.time()

    with open(file_path, 'r', encoding='Windows-1252') as f: # Se usa la codicifación Windows-1252 para que funcione con el archivo de referencia dado.
        text = f.read()                                      # Para casos generales se usaría la codicifación UTF-8.
    text.replace('\t', ' ')
    dictionary = {bytes([i]): i for i in range(256)}
    result = []
    w = b""

    for c in text.encode('Windows-1252'):
        wc = w + bytes([c])
        try:
            if wc in dictionary:
                w = wc
            else:
                result.append(dictionary[w])
                dictionary[wc] = len(dictionary)
                w = bytes([c])
        except KeyError:
            pass
    if w:
        result.append(dictionary[w])

    result = np.array(result, dtype=np.uint32)
    with open('comprimido.elmejorprofesor', 'wb') as f:
        result.tofile(f)

    end_time = time.time()
    print("Tiempo de compresión:", end_time - start_time, "segundos")
