from gambas.manager import ConfigContentManager, JsonContentManager

def get_manager(filepath):
  file_ext = filepath.split(".")[-1]
  if file_ext == "cfg":
    manager = ConfigContentManager(filepath)
  elif file_ext == "json":
    manager = JsonContentManager(filepath)
  return manager
