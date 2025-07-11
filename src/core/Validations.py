import os
import hashlib
import zipfile

class Validations:
  def get_hash_file(self, zip_path, algorithm='sha256'):
    required_exts = ['.shp', '.shx', '.dbf']
    hash_func = hashlib.new(algorithm)
    
    try: 
      with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        files = zip_ref.namelist()
        base_names = {}
        
        for file in files:
          ext = os.path.splitext(file)[1].lower()
          if ext in required_exts:
            base_name = os.path.splitext(file)[0]
            base_names[base_name] = base_names.get(base_name, set())
            base_names[base_name].add(ext)
        
        for base, exts in base_names.items():
          if all(ext in exts for ext in required_exts):
            for ext in required_exts:
              full_path = f"{base}{ext}"
              with zip_ref.open(full_path) as f:
                while chunk := f.read(8192):
                  hash_func.update(chunk)
            return hash_func.hexdigest()
            
            
      return "Shapefile incompleto no zip"
    
    except Exception as e:
      return f"Erro ao processar zip: {e}" 
            
    
    
  def compare_hashes(self, hash1, hash2):
    return hash1 == hash2
  
  def is_shapefile(self, file_path):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
      file_names = zip_ref.namelist()
      shapefile_exts = {'.shp', '.shx', '.dbf'}
      found = {ext: False for ext in shapefile_exts}
      
      for name in file_names:
        for ext in shapefile_exts:
          if name.lower().endswith(ext):
            found[ext] = True
    
    return all(found.values())
      # return all(name.endswith(ext) for name in file_names for ext in ['.shp', '.shx', '.dbf'])