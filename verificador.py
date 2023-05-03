import os
def verify(original_file_path, decompressed_file_path):
    with open(original_file_path, 'rb') as f1, open(decompressed_file_path, 'rb') as f2:
        total_bytes = os.path.getsize(original_file_path)
        different_bytes = 0        
        while True:
            byte1 = f1.read()
            byte2 = f2.read()
            
            if byte1 != byte2:
                different_bytes += 1
            
            if not byte1:
                break
        
        similarity = (1 - (different_bytes / total_bytes)) * 100
        print(f"Similaridad: {similarity:.2f}%")
        
        if similarity == 100:
            print("Ok")
            
        else:
            print("NOk")