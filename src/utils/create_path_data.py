from datetime import datetime
from project_routes import Routes

class DownloaderOutputPath:
  def __init__(self):
    self.routes = Routes()
    
  def get_output_path(self, embargo_name):
    month_map = {
        1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
        7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'
    }
    
    date_now = datetime.now()
    day = date_now.strftime("%d")
    month = month_map[int(date_now.strftime("%m"))]
    year = date_now.strftime("%Y")
  
    output_path = self.routes.data_path() + f"/{embargo_name}/{year}/{month}/{day}"
    
    return output_path
  
  

