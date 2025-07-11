from src.config.bases_infos import EMBARGOS_DATA_SOURCES
from src.utils.check_link import CheckLink
from src.config.logger_config import LoggerConfig
from src.core.Downloader import Downloader
from src.core.Validations import Validations
from src.utils.templates import Templates

import asyncio
import project_routes

ROUTES = project_routes.Routes()

def logget_teste():
  logger_config = LoggerConfig()
  logger = logger_config.get_logger()
  
  logger.info("Iniciando o processo de validação de links das fontes de dados de embargos.")
  logger.info(f"Total de fontes de dados: {len(EMBARGOS_DATA_SOURCES)}")
  
  
  logger_config.export_log(prefix="embargos_log")
  
async def check_links():
  logger_config = LoggerConfig()
  logger = logger_config.get_logger()
  
  template = Templates()
  
  downloader = Downloader()
  validation = Validations()
  
  status = []
  for i, source in EMBARGOS_DATA_SOURCES.items():
    output_path = ROUTES.get_output_path(source.name)
    for dataset in source.datasets:
      # TODO Fazer a verificação do link
      check_link = await CheckLink.create(dataset.url)
      
      print(template.get_str_result_check_links(check_link))
      # logger.info(check_link.print_result())
      
    #   result = downloader.download(
    #     url=dataset.url, 
    #     file_name=dataset.file_name, 
    #     file_path=output_path
    #   )
      
    #   # TODO Verificação se é shapefile
      
  
  logger_config.export_log(prefix="embargos_log") 
  
  return status


  
if __name__ == "__main__":
    # asyncio.run(main())
    asyncio.run(check_links())
