import time
import numpy as np
def decompress(file_path):
    start_time = time.time()

    with open(file_path, 'rb') as f:
        data = f.read()

    compressed_data = np.frombuffer(data, dtype=np.uint32)
    dictionary = {i: bytes([i]) for i in range(256)}
    result = bytearray()
    w = bytes([compressed_data[0]])

    for k in compressed_data[1:]:
        if k in dictionary:
            entry = dictionary[k]
        else:
            entry = w + bytes([w[0]])
        result.extend(entry)
        dictionary[len(dictionary)] = w + bytes([entry[0]])
        w = entry
    with open("descomprimido-elmejorprofesor.txt", 'wb') as f:
        f.write(result)

    end_time = time.time()
    print("Tiempo de descompresión:", end_time - start_time, "segundos")