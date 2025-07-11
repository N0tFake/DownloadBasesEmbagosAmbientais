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
        slug="Embargos IBAMA",
        url="https://pamgia.ibama.gov.br/geoservicos/arquivos/adm_embargo_ibama_a.shp.zip",
        file_name="SITE_embargos_ibama.zip"
      )
    ]
  ),
  
  Orgao.ICMBIO: DataSourceInfo(
    name="ICMbio",
    datasets=[
      DatasetsInfo(
        slug="Embargos ICMbio",
        url="https://www.gov.br/icmbio/pt-br/assuntos/dados_geoespaciais/mapa-tematico-e-dados-geoestatisticos-das-unidades-de-conservacao-federais/embargos_icmbio_shp.zip",
        file_name="SITE_embargos_icmbio.zip"
      )
    ]
  ),
  
  Orgao.SEMA_MT: DataSourceInfo(
    name="SEMA_MT",
    datasets=[
      DatasetsInfo(
        slug="Embargos SEMA MT",
        url="https://geo.sema.mt.gov.br/geoserver/wfs?authkey=541085de-9a2e-454e-bdba-eb3d57a2f492&request=getfeature&service=wfs&version=1.0.0&typename=Geoportal:AREAS_EMBARGADAS_SEMA&outputformat=SHAPE-ZIP",
        file_name="SITE_embargos_sema_mt.zip"
      )
    ]
  ),
  
  Orgao.SIGA_MT: DataSourceInfo(
    name = "SIGA_MT",
    datasets = [
      DatasetsInfo(
        slug="Embargos SIGA MT Polígono",
        url="https://geo.sema.mt.gov.br/geoserver/wfs?authkey=541085de-9a2e-454e-bdba-eb3d57a2f492&request=getfeature&service=wfs&version=1.0.0&typename=Geoportal:AREA_EMBARGADA_SIGA_POLIGONO&outputformat=SHAPE-ZIP",
        file_name="SITE_embargos_siga_poligono_mt.zip"
      ),
      DatasetsInfo(
        slug="Embargos SIGA MT Ponto",
        url="https://geo.sema.mt.gov.br/geoserver/wfs?authkey=541085de-9a2e-454e-bdba-eb3d57a2f492&request=getfeature&service=wfs&version=1.0.0&typename=Geoportal:AREA_EMBARGADA_SIGA_PONTO&outputformat=SHAPE-ZIP",
        file_name="SITE_embargos_siga_ponto_mt.zip"
      )
    ],
  ),

  Orgao.SIMGEO: DataSourceInfo(
    name = "SIMGEO",
    datasets = [
      DatasetsInfo(
        slug="Embargos SIMGEO",
        url="http://www.sema.mt.gov.br/transparencia/index.php/documentos/25/Dados-de-Desmatamento/2813/Base-de-Desmatamento-de-2018.zip",
        file_name="SITE_embargos_simgeo_mt.zip"
      )
    ],
  ),
  
  Orgao.LDI:  DataSourceInfo(
    name = "LDI",
    datasets = [  
      DatasetsInfo(
        slug="Embargos LDI manual",
        url="https://monitoramento.semas.pa.gov.br/ldi/regioesdesmatamento/baixartodosshapefile?tipoShape=MANUAL",
        file_name="SITE_embargos_LDI_manual.zip"
      ),
      DatasetsInfo(
        slug="Embargos LDI automatizado",
        url="https://monitoramento.semas.pa.gov.br/ldi/regioesdesmatamento/baixartodosshapefile?tipoShape=AUTOMATIZADO",
        file_name="SITE_embargos_LDI_automatico.zip"
      ),
      DatasetsInfo(
        slug="Embargos LDI sem sobreposição",
        url="https://monitoramento.semas.pa.gov.br/ldi/regioesdesmatamento/baixartodosshapefile?tipoShape=SEMSOBREPOSICAO",
        file_name="SITE_embargos_LDI_sem_sobreposicao.zip"
      )
    ] 
  ),
}
