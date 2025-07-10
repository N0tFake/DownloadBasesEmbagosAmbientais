from enum import Enum
from dataclasses import dataclass

class Orgao(Enum):
    IBAMA = "IBAMA"
    ICMBIO = "ICMbio"
    SEMA_MT = "SEMA_MT"
    SIGA_MT = "SIGA_MT"
    SIMGEO = "SIMGEO"
    LDI = "LDI"

@dataclass(frozen=True)
class DataSourceInfo:
    name: str
    datasets: list

@dataclass(frozen=True)
class DatasetsInfo:
    slug: str
    url: str
    file_name: str

    

EMBARGOS_DATA_SOURCES = {
  
  Orgao.IBAMA: DataSourceInfo(
    name="IBAMA",
    datasets=[
      DatasetsInfo(
        slug="embargos_ibama",
        url="https://pamgia.ibama.gov.br/geoservicos/arquivos/adm_embargo_ibama_a.shp.zip",
        file_name="embargos_ibama.zip"
      )
    ]
  ),
  
  Orgao.ICMBIO: DataSourceInfo(
    name="ICMbio",
    datasets=[
      DatasetsInfo(
        slug="embargos_icmbio",
        url="https://www.gov.br/icmbio/pt-br/assuntos/dados_geoespaciais/mapa-tematico-e-dados-geoestatisticos-das-unidades-de-conservacao-federais/embargos_icmbio_shp.zip",
        file_name="embargos_icmbio_shp.zip"
      )
    ]
  ),
  
  Orgao.SEMA_MT: DataSourceInfo(
    name="SEMA_MT",
    datasets=[
      DatasetsInfo(
        slug="embargos_sema_mt",
        url="https://geo.sema.mt.gov.br/geoserver/wfs?authkey=541085de-9a2e-454e-bdba-eb3d57a2f492&request=getfeature&service=wfs&version=1.0.0&typename=Geoportal:AREAS_EMBARGADAS_SEMA&outputformat=SHAPE-ZIP",
        file_name="embargos_sema_mt.zip"
      )
    ]
  ),
  
  Orgao.SIGA_MT: DataSourceInfo(
    name = "SIGA_MT",
    datasets = [
      DatasetsInfo(
        slug="embargos_siga_poligono_mt",
        url="https://geo.sema.mt.gov.br/geoserver/wfs?authkey=541085de-9a2e-454e-bdba-eb3d57a2f492&request=getfeature&service=wfs&version=1.0.0&typename=Geoportal:AREA_EMBARGADA_SIGA_POLIGONO&outputformat=SHAPE-ZIP",
        file_name="embargos_siga_poligono_mt.zip"
      ),
      DatasetsInfo(
        slug="embargos_siga_ponto_mt",
        url="https://geo.sema.mt.gov.br/geoserver/wfs?authkey=541085de-9a2e-454e-bdba-eb3d57a2f492&request=getfeature&service=wfs&version=1.0.0&typename=Geoportal:AREA_EMBARGADA_SIGA_PONTO&outputformat=SHAPE-ZIP",
        file_name="embargos_siga_ponto_mt.zip"
      )
    ],
  ),

  Orgao.SIMGEO: DataSourceInfo(
    name = "SIMGEO",
    datasets = [
      DatasetsInfo(
        slug="embargos_simgeo_mt",
        url="http://www.sema.mt.gov.br/transparencia/index.php/documentos/25/Dados-de-Desmatamento/2813/Base-de-Desmatamento-de-2018.zip",
        file_name="embargos_simgeo_mt.zip"
      )
    ],
  ),
  
  Orgao.LDI:  DataSourceInfo(
    name = "LDI",
    datasets = [  
      DatasetsInfo(
        slug="embargos_LDI_manual",
        url="https://monitoramento.semas.pa.gov.br/ldi/regioesdesmatamento/baixartodosshapefile?tipoShape=MANUAL",
        file_name="embargos_LDI_manual.zip"
      ),
      DatasetsInfo(
        slug="embargos_LDI_automatico",
        url="https://monitoramento.semas.pa.gov.br/ldi/regioesdesmatamento/baixartodosshapefile?tipoShape=AUTOMATIZADO",
        file_name="embargos_LDI_automatico.zip"
      ),
      DatasetsInfo(
        slug="embargos_LDI_sem_sobreposicao",
        url="https://monitoramento.semas.pa.gov.br/ldi/regioesdesmatamento/baixartodosshapefile?tipoShape=SEMSOBREPOSICAO",
        file_name="embargos_LDI_sem_sobreposicao.zip"
      )
    ] 
  ),
}
