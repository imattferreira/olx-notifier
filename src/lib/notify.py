import os

def _install_deps() -> None:
  os.system("brew install terminal-notifier")

def _has_necessary_deps() -> bool:
   # TODO get stdout
  stdout = ""
  os.system("brew list | grep terminal-notifier")

  return bool(stdout)

def notify(
  icon: str, 
  link: str, 
  message: str, 
  title: str
):
  app_icon = "src/imgs/olx.png"
  command = f"terminal-notifier -appIcon {app_icon} -message \"{message}\" -title \"{title}\" -open \"{link}\" -contentImage \"{icon}\" -sound default" 

  if not _has_necessary_deps():
    _install_deps()
  
  os.system(command)