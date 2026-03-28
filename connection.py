def function():
    raise ConnectionError 
try:
     function()
except ConnectionError as exe:
      raise RuntimeError("failed to open database",exe)