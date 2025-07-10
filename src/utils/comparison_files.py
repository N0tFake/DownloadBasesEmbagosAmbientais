import os
import hashlib

def get_hash_file(file_path_base, algorithm='sha256'):
  extensions = ['.shp', '.shx', '.dbf']
  hash_func = hashlib.new(algorithm)
  
  for ext in extensions:
    file_path = file_path_base + ext
    if not os.path.exists(file_path):
      raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, 'rb') as f:
      while chunk := f.read(8192):
        hash_func.update(chunk)
    
  return hash_func.hexdigest()
