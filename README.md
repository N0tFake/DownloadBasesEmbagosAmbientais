# GetBasesEmbargos

## Descrição

Este projeto é um script Python desenvolvido para automatizar o download e validação de bases de dados geoespaciais, especificamente voltado para bases de dados de embargos. O sistema realiza verificações abrangentes para garantir a integridade e qualidade dos dados baixados.

## Funcionalidades

### 🔍 Verificações Automáticas
- **Validação de Links**: Verifica se os links para download estão ativos e acessíveis
- **Verificação de Dados Novos**: Identifica se há atualizações disponíveis nas bases de dados
- **Validação de Shapefiles**: Verifica a integridade dos arquivos shapefiles
- **Verificação de Codificação**: Garante que os dados estão com a codificação correta (UTF-8)
- **Detecção de Caracteres Quebrados**: Identifica e reporta problemas de encoding nos dados

### 📊 Processamento de Dados
- Download automatizado de bases de dados
- Validação de integridade dos arquivos
- Verificação de estrutura dos shapefiles
- Relatórios de status e erros

## Pré-requisitos

- Python 3.7 ou superior
- Bibliotecas Python necessárias (ver `requirements.txt`)

## Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd GetBasesEmbargos
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

### Execução Básica
```bash
python main.py
```

### Parâmetros Disponíveis
```bash
python main.py --help
```

## Estrutura do Projeto

```
GetBasesEmbargos/
├── main.py                 # Script principal
├── requirements.txt        # Dependências do projeto
├── config/                 # Arquivos de configuração
├── data/                   # Dados baixados
├── logs/                   # Arquivos de log
└── utils/                  # Utilitários e funções auxiliares
```

## Configuração

As configurações do projeto podem ser ajustadas no arquivo `config/config.json`:

```json
{
    "download_path": "./data",
    "log_level": "INFO",
    "encoding": "utf-8",
    "timeout": 30,
    "retry_attempts": 3
}
```

## Logs e Relatórios

O sistema gera logs detalhados das operações realizadas:

- **Logs de Download**: Registro de todos os downloads realizados
- **Logs de Validação**: Resultados das verificações de integridade
- **Relatórios de Erro**: Detalhes sobre problemas encontrados
- **Relatórios de Status**: Resumo geral das operações

## Validações Realizadas

### 1. Verificação de Links
- Teste de conectividade com os servidores
- Validação de URLs de download
- Verificação de disponibilidade dos recursos

### 2. Validação de Shapefiles
- Verificação da estrutura dos arquivos .shp, .shx, .dbf
- Validação de geometrias
- Verificação de sistema de coordenadas

### 3. Verificação de Codificação
- Detecção automática de encoding
- Conversão para UTF-8 quando necessário
- Identificação de caracteres especiais problemáticos

### 4. Verificação de Novos Dados
- Comparação de timestamps
- Verificação de checksums
- Detecção de mudanças no conteúdo

## Tratamento de Erros

O sistema implementa tratamento robusto de erros:

- **Conexão**: Retry automático em caso de falha de rede
- **Dados Corrompidos**: Detecção e relatório de arquivos corrompidos
- **Encoding**: Tentativa de correção automática de problemas de codificação
- **Geometrias Inválidas**: Identificação e relatório de geometrias problemáticas

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Contato

Para dúvidas ou sugestões, entre em contato através de:
- Email: [seu-email@exemplo.com]
- Issues: [Link para issues do repositório]

## Changelog

### v1.0.0
- Implementação inicial do sistema de download
- Validação básica de shapefiles
- Sistema de logs

### Próximas Versões
- [ ] Interface gráfica
- [ ] Suporte a mais formatos de dados
- [ ] Integração com APIs de dados governamentais
- [ ] Dashboard de monitoramento

---

**Nota**: Este projeto foi desenvolvido para automatizar o processo de obtenção e validação de bases de dados geoespaciais, garantindo a qualidade e integridade das informações utilizadas em análises posteriores.