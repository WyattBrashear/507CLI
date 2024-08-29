import AWESOMECALC
import Sysdiagnostics
import writer

def execute(appid):
  if appid == 1:
    AWESOMECALC.awesomecalc()
  if appid == 2:
    Sysdiagnostics.startdiagnostics()
  if appid == 3:
    writer.writer()