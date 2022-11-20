def error(*args):
  resultado=0
  for numero in args: 
    try:
      resultado=+numero 
      print(resultado)
    