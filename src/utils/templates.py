class Templates:

  def __init__(self):
    self.MAX_WIDTH = 120
    self.BORDER_TOP = f"┌{'─' * self.MAX_WIDTH}┐"
    self.BORDER_BOTTOM = f"└{'─' * self.MAX_WIDTH}┘"
    self.PAD = "│"
    self.PREFIX = "Embargo: "

  def get_str_result_check_links(self, check_link_result, name=""):
    title_line = f"{name}".strip()
    if len(title_line) > self.MAX_WIDTH:
      title_line = title_line[:self.MAX_WIDTH - 3] + "..."
    title_line = f"{self.PAD} {title_line}".ljust(self.MAX_WIDTH + 1) + self.PAD

    lines = [
      self.BORDER_TOP,
      title_line,
      f"{self.PAD}{'─' * self.MAX_WIDTH}{self.PAD}",
      self.__format_line("URL: ", check_link_result.url),
      self.__format_line("Status: ", f"{check_link_result.status_code} - {check_link_result.status_message}"),
      self.__format_line("Válido: ", "", icon='✅' if check_link_result.is_valid else '❌'),
      self.__format_line("Arquivo compactado: ", "", icon='✅' if check_link_result.is_compacted_file else '❌'),
    ]

    if not check_link_result.is_valid:
      lines.append(self.__format_line("Tipo de erro: ", check_link_result.error_type))
      lines.append(self.__format_line("Mensagem: ", check_link_result.error_message))

    lines.append(self.BORDER_BOTTOM)
    return "\n".join("\t" + line for line in lines)
    
  def __format_line(self, label, value, icon=None):
    val_str = f"{icon} {value}" if icon else str(value)
    full_text = f"{label}{val_str}"

    if len(full_text) > self.MAX_WIDTH:
        full_text = full_text[:self.MAX_WIDTH - 5] + "..."
    return f"{self.PAD} {full_text}".ljust(self.MAX_WIDTH + 1) + self.PAD


