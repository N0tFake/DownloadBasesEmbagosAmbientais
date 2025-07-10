import logging
import datetime
from pathlib import Path
from project_routes import Routes

class LoggerConfig():
  def __init__(self, name="GetBasesEmbargos", level=logging.INFO):
    self.logger = logging.getLogger(name)
    self.logger.setLevel(level)

    ch = logging.StreamHandler()
    ch.setLevel(level)

    formatter = logging.Formatter('[%(asctime)s] %(name)s - %(levelname)s: %(message)s')
    ch.setFormatter(formatter)
    
    self.logger.addHandler(ch)
    
    self.log_messages = []
    memory_handler = MemoryHandler(self.log_messages)
    memory_handler.setLevel(level)
    memory_handler.setFormatter(formatter)
    self.logger.addHandler(memory_handler)
    
  def get_logger(self):
    return self.logger
  
  def export_log(self, prefix="log"):
    now = datetime.datetime.now()
    filename = f"{prefix}_{now.strftime('%Y%m%d_%H%M%S')}.txt"
    
    log_path = Path(Routes().log_path())
    log_path.mkdir(parents=True, exist_ok=True)
    
    file_path = log_path / filename
    
    try:
      with open(file_path, "w", encoding="utf-8") as f:
        if self.log_messages:
          for message in self.log_messages:
            f.write(message + "\n")
        else:
          f.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] No log messages found.\n")
      self.logger.info(f"Log exported successfully to: {file_path}")
      
    except Exception as e:
      self.logger.error(f"Failed to export log: {e}")
      return None
    
    return filename

  def clear_log_memory(self):
    self.log_messages.clear()
  
class MemoryHandler(logging.Handler):
    def __init__(self, log_storage):
        super().__init__()
        self.log_storage = log_storage
    
    def emit(self, record):
        try:
            msg = self.format(record)
            self.log_storage.append(msg)
        except Exception:
            self.handleError(record)
    