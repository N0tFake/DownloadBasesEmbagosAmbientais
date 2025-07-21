from src.config.bases_infos import EMBARGOS_DATA_SOURCES, Orgao
from src.utils.check_link import CheckLink
from src.config.logger_config import LoggerConfig
from src.core.Downloader import Downloader
from src.core.Validations import Validations
from src.utils.templates import Templates
from src.utils.compression_detector import CheckCompactedFileLocal

from datetime import datetime, date

import os
import asyncio
import project_routes
import sqlite3
import pathlib as Path
import zipfile

EMBARGOS_NAME = Orgao
ROUTES = project_routes.Routes()
LOGGER = LoggerConfig().get_logger()
TEMPLATES = Templates()

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
      
      logger.info(f"Download Embargo: {dataset.slug}")
      for index_url, url in enumerate(dataset.urls):
        logger.info(f"Downloader com link {index_url + 1}: {url}")
        result = downloader.download(
          url=url,
          file_name=dataset.file_name,
          file_path=output_path
        )
        if result['success']:
          logger.info(f"Download realizado com sucesso: {result['path']}")
          # TODO Verificação se é shapefile
    
        else:
          logger.error(f"Erro ao baixar o arquivo: {dataset.file_name} da URL: {url}")
          logger.error(f"Erro: {result['error']}")
          continue

  logger_config.export_log(prefix="embargos_log")

  # return status

def compare_hash():
  
  validations = Validations()
  routes = project_routes.Routes()
  
  map_name_files = {
    "IBAMA": {
      "NAME": 'IBAMA',
      "MANUAL": 'adm_embargo_ibama_a.shp.zip',
      "AUTO": "SITE_embargos_ibama.zip"
    },
    "ICMbio": {
      "NAME": 'ICMbio',
      "MANUAL": "embargos_icmbio.zip",
      "AUTO": "SITE_embargos_icmbio.zip"
    },
    "LDI_AUTOMATIZADO": {
      "NAME": 'LDI',
      "MANUAL": "LDI_publicacao_automatizado.zip",
      "AUTO": "SITE_embargos_LDI_automatico.zip"
    },
    "LDI_MANUAL": {
      "NAME": 'LDI',
      'MANUAL': "LDI_publicacao_manual.zip",
      'AUTO': "SITE_embargos_LDI_manual.zip"
    },
    "LDI_SEM_SOBREPOSICAO": {
      "NAME": 'LDI',
      'MANUAL': "LDI_publicacao_sem_sobresicao.zip",
      'AUTO': "SITE_embargos_LDI_sem_sobreposicao.zip"
    },
    "SEMA_MT": {
      "NAME": 'SEMA_MT',
      'MANUAL': "AREAS_EMBARGADAS_SEMA.zip",
      'AUTO': "SITE_embargos_sema_mt.zip"
    },
    "SIGA_POLIGONO": {
      "NAME": 'SIGA_MT',
      'MANUAL': "AREA_EMBARGADA_SIGA_POLIGONO.zip",
      'AUTO': "SITE_embargos_siga_poligono_mt.zip"
    },
    "SIGA_PONTO": {
      "NAME": 'SIGA_MT',
      'MANUAL': "AREA_EMBARGADA_SIGA_PONTO.zip",
      'AUTO': "SITE_embargos_siga_ponto_mt.zip"
    }
  }
  
  result_map = {
    'data': datetime.now().strftime("%Y-%m-%d"),
    'IBAMA': {
      'path_auto': '',
      'path_manual': '',
      'hash_auto': '',
      'hash_manual': '',
      'compare': False
    },
    'ICMbio': {
      'path_auto': '',
      'path_manual': '',
      'hash_auto': '',
      'hash_manual': '',
      'compare': False
    },
    'LDI': {
      'LDI_AUTOMATIZADO': {
        'path_auto': '',
        'path_manual': '',
        'hash_auto': '',
        'hash_manual': '',
        'compare': False
      },
      'LDI_MANUAL': {
        'path_auto': '',
        'path_manual': '',
        'hash_auto': '',
        'hash_manual': '',
        'compare': False
      },
      'LDI_SEM_SOBREPOSICAO': {
        'path_auto': '',
        'path_manual': '',
        'hash_auto': '',
        'hash_manual': '',
        'compare': False
      }
    },
    'SEMA_MT': {
      'path_auto': '',
      'path_manual': '',
      'hash_auto': '',
      'hash_manual': '',
      'compare': False
    },
    
    'SIGA_MT': {
      'SIGA_POLIGONO': {
        'path_auto': '',
        'path_manual': '',
        'hash_auto': '',
        'hash_manual': '',
        'compare': False
      },
      'SIGA_PONTO': {
        'path_auto': '',
        'path_manual': '',
        'hash_auto': '',
        'hash_manual': '',
        'compare': False
      }
    }
  }
  
  for key, value in map_name_files.items():
    
    file_auto = routes.get_output_path(embargo_name=value['NAME']).joinpath(value['AUTO'])
    file_manual = routes.get_output_path_manual(embargo_name=value['NAME']).joinpath(value['MANUAL'])
    
  
    hash_auto = validations.get_hash_file(zip_path=file_auto)
    hash_manual = validations.get_hash_file(zip_path=file_manual)
    
    file_auto = file_auto
    file_manual = file_manual
    
    if value['NAME'] == 'LDI':
      result_map[value['NAME']][key] = {
        'path_auto': file_auto,
        'path_manual': file_manual,
        'hash_auto': hash_auto,
        'hash_manual': hash_manual,
        'compare': validations.compare_hashes(hash1=hash_auto, hash2=hash_manual)
      }
    elif value['NAME'] == 'SIGA_MT':
      result_map[value['NAME']][key] = {
        'path_auto': file_auto,
        'path_manual': file_manual,
        'hash_auto': hash_auto,
        'hash_manual': hash_manual,
        'compare': validations.compare_hashes(hash1=hash_auto, hash2=hash_manual)
      }
    else:
      result_map[value['NAME']]['path_auto'] = file_auto
      result_map[value['NAME']]['path_manual'] = file_manual
      result_map[value['NAME']]['hash_auto'] = hash_auto
      result_map[value['NAME']]['hash_manual'] = hash_manual
      result_map[value['NAME']]['compare'] = validations.compare_hashes(hash1=hash_auto, hash2=hash_manual)
   
  with open(routes.log_hash_comparete(), 'a') as f:
    f.write(f"\n\nData: {result_map['data']}\n")
    for key, value in result_map.items():
      if key == 'data':
        continue
      
      f.write(f"{key}:\n")
      if key in ['LDI', 'SIGA_MT']:
        for sub_key, sub_value in value.items():
          f.write(f"  {sub_key}:\n")
          f.write(f"    Path Auto: {str(sub_value['path_auto'])}\n")
          f.write(f"    Path Manual: {str(sub_value['path_manual'])}\n")
          f.write(f"    Hash Auto: {sub_value['hash_auto']}\n")
          f.write(f"    Hash Manual: {sub_value['hash_manual']}\n")
          f.write(f"    Compare: {sub_value['compare']}\n")
      else:
        f.write(f"  Path Auto: {str(value['path_auto'])}\n")
        f.write(f"  Path Manual: {str(value['path_manual'])}\n")
        f.write(f"  Hash Auto: {value['hash_auto']}\n")
        f.write(f"  Hash Manual: {value['hash_manual']}\n")
        f.write(f"  Compare: {value['compare']}\n")
    
    f.write("-" * 100 + "\n")
  
def list_compact_files():
  #TODO Pegar caminho de arquivos do dia anterior
  for source in EMBARGOS_DATA_SOURCES.values():
    output_path = ROUTES.get_output_path(source.name)
    for f in os.listdir(output_path):
      is_compact = CheckCompactedFileLocal(
        path_file=output_path.joinpath(f)
      ).is_valid()
      
      # if is_compact:
        
def created_databese_sqlite():
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS infos (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      file TEXT NOT NULL,
      embargo TEXT NOT NULL,
      date_download TEXT NOT NULL,
      hash TEXT NOT NULL,
      file_size INTEGER NOT NULL,
      file_date_created TEXT NOT NULL,
      previous_file_id INTEGER,
      is_new_file_id INTEGER,
      is_last_download INTEGER,
    )              
  ''')
  
  conn.commit()
  conn.close()
  
def save_data(): 
  # 
  
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  
  data = (
    'file_name.zip',  # file
    'embargo_name',  # embargo
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # date_download
    'hash_value',  # hash
    123456,  # file_size
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # file_date_created
    None,  # previous_file_id
    1,  # is_new_file_id
    1   # is_last_download
  )
  
  insert_query = '''
    INSERT INTO infos (file, embargo, date_download, hash, file_size, file_date_created, previous_file_id, is_new_file_id, is_last_download)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)               
  '''
  
  cursor.execute(insert_query, data)
  conn.commit()
  conn.close()
  
def list_infos_db():
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  
  cursor.execute('SELECT * FROM infos')
  rows = cursor.fetchall()
  
  for row in rows:
    print(row)
  
  conn.close()  

def get_metadata(file_path):
  with zipfile.ZipFile(file_path, 'r') as zip_ref:
    
    file_names = zip_ref.namelist()
    size_total = 0
    create_date = None
    
    for info in zip_ref.infolist():
      size_total += info.file_size
      create_date = datetime(
        info.date_time[0], 
        info.date_time[1], 
        info.date_time[2], 
        info.date_time[3], 
        info.date_time[4], 
        info.date_time[5]
      )
  
  return {
    'file_names': file_names,
    'size_total': size_total,
    'create_date': create_date,
  }
    
async def handle_check_link():

  result_stats = {}
  
  for i, source in EMBARGOS_DATA_SOURCES.items():
    for dataset in source.datasets:
      check_link = await CheckLink.create(dataset.url)
      result = check_link.result_dict()
      print(TEMPLATES.get_str_result_check_links(check_link, dataset.slug))
      

    
if __name__ == "__main__":
  # list_compact_files()
  # handle_sqlite()


  # asyncio.run(check_links())
  
  
  # asyncio.run(handle_check_link())
  
  # compare_hash()

  # created_databese_sqlite()
  # save_data()
  # list_infos_db()

  # get_metadata()
  


  ...