import magic
import aiohttp

COMPACTED_TYPES = [
  'zip',
  'gzip',
  'bzip2',
  'xz',
  'rar',
  '7z'
]

CONTENT_TYPE_TO_COMPRESSION = {
  'application/zip': 'zip',
  'application/x-zip-compressed': 'zip',
  'application/gzip': 'gzip',
  'application/x-bzip2': 'bzip2',
  'application/x-xz': 'xz',
  'application/x-rar': 'rar',
  'application/x-7z-compressed': '7z',
}

MAGIC_SIGNATURES = {
  b'PK\x03\x04': 'zip',
  b'PK\x05\x06': 'zip',
  b'\x1f\x8b\x08': 'gzip',
  b'BZh': 'bzip2',
  b'\xfd7zXZ\x00': 'xz',
  b'Rar!\x1a\x07\x00': 'rar',
  b'7z\xbc\xaf\x27\x1c': '7z'
}

class CheckCompactedFile:
  
  def __init__(self, url_or_response):
    self.url_or_response = url_or_response
    self.cached_bytes = None
    self._content_type = None
  
  async def is_valid(self):
    compresion_type = await self.__get_type_compression()
    return compresion_type in COMPACTED_TYPES if compresion_type else False

  async def __get_type_compression(self):
    content_type = self.__get_content_type()
    
    if content_type:
      compression_type = CONTENT_TYPE_TO_COMPRESSION.get(content_type)
      if compression_type:
        return compression_type
      
      if content_type == 'application/octet-stream':
        return await self.__check_if_octet_stream_is_compacted_file()
    
    return None

  def __get_content_type(self):
    if isinstance(self.url_or_response, aiohttp.ClientResponse):
      return self.url_or_response.headers.get('Content-Type')
    
    elif isinstance(self.url_or_response, str):
      return self.__local_file_is_compacted(self.url_or_response)
      
    else:
      return None

  async def __check_if_octet_stream_is_compacted_file(self):
    try:
      peek_data = await self.url_or_response.content.read(512) 
      for magic_signature, comp_type in MAGIC_SIGNATURES.items():
          if peek_data.startswith(magic_signature):
              return comp_type
    except Exception as e:
        return None

    return None
      
  def __local_file_is_compacted(self, path_file):
    try:
      mime = magic.Magic(mime=True)
      file_mime = mime.from_file(path_file)
      
      return file_mime if file_mime in CONTENT_TYPE_TO_COMPRESSION else None
    
    except Exception as e:
      print(f"Error detecting compression type: {e}")
      return None
