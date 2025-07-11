from datetime import datetime
import os
from pathlib import Path

PROJECT_PATH = Path(__file__).parent.absolute()

class Routes:
  
  def project_path(self):
    return PROJECT_PATH
  
  def log_path(self):
    return os.path.join(PROJECT_PATH, "logs")
  
  def data_path(self):
    return os.path.join(PROJECT_PATH, "data")
  
  def get_output_path(self, embargo_name):
    month_map = {
        1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
        7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'
    }
    
    date_now = datetime.now()
    day = date_now.strftime("%d")
    month = month_map[int(date_now.strftime("%m"))]
    year = date_now.strftime("%Y")
  
    output_path = Path(r'C:\Users\silvio.chaves\Desktop\MAIN\Atualizações de Bases\Embargos').joinpath(embargo_name, year, month, day)
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path
    
    output_path = Path(self.data_path()).joinpath(embargo_name, year, month, day)
    output_path.mkdir(parents=True, exist_ok=True)
    
    return output_path