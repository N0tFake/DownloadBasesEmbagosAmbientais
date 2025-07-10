import os
from pathlib import Path

# Pasta do arquivo atual
PROJECT_PATH = Path(__file__).parent.absolute()


class Routes:
  
  def project_path(self):
    return PROJECT_PATH
  
  def log_path(self):
    return os.path.join(PROJECT_PATH, "logs")