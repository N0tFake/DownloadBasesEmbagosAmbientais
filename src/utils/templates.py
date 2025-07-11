class Templates:
  def get_str_result_check_links(self, check_link_result):
    result = "\n"
    result += f"\t┌{'-'*120}\n"
    result += f"\t| URL: {check_link_result.url}\n"
    result += f"\t| Status: {check_link_result.status_code} - {check_link_result.status_message}\n"
    result += f"\t| Válido: {'✅' if check_link_result.is_valid else '❌' }\n"
    result += f"\t| Arquivo compactado: {'✅' if check_link_result.is_compacted_file else '❌'}\n"
    
    if not check_link_result.is_valid:
        result += f"\t| Tipo de erro: {check_link_result.error_type}\n"
        result += f"\t| Mensagem: {check_link_result.error_message}\n"
    
    result += f"\t└{'-'*120}\n"
    
    return result