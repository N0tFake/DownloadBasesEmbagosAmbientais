from src.config.bases_infos import EMBARGOS_DATA_SOURCES
from src.utils.check_link import CheckLink
from src.config.logger_config import LoggerConfig
import asyncio
import project_routes

# async def main():
#   count = 0
#   for i, values in EMBARGOS_DATA_SOURCES.items():
#     count += 1
#     print(f"\nFonte de dados: {values.name}")
#     for dataset in values.datasets:
#       checker = await CheckLink.create(dataset.url)
#       checker.print_result()  
      
#   print(f"Total de fontes de dados: {count}")
  

def main():
  logger_config = LoggerConfig()
  logger = logger_config.get_logger()
  
  logger.info("Iniciando o processo de validação de links das fontes de dados de embargos.")
  logger.info(f"Total de fontes de dados: {len(EMBARGOS_DATA_SOURCES)}")
  
  logger_config.export_log(prefix="embargos_validation_log")
  
if __name__ == "__main__":
    # asyncio.run(main())
    routes = project_routes.Routes()
    print(routes.project_path())
    main()