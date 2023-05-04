import time
import numpy as np
import struct

def compress(file_path):
    start_time = time.time()

    with open(file_path, 'rb') as f:
        data = f.read()
    dictionary = {bytes([i]): i for i in range(256)}
    result = []
    w = b""

    for c in data:
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

    compressed_data = np.array(result, dtype=np.uint32)

    # Convertir los datos comprimidos a una cadena de bytes estructurada
    compressed_bytes = struct.pack(f'<{len(compressed_data)}I', *compressed_data)

    with open('comprimido.elmejorprofesor', 'wb') as f:
        f.write(compressed_bytes)

    end_time = time.time()
    print("Tiempo de compresión:", end_time - start_time, "segundos")
