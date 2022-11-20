def error(*args):
  resultado=0
  for numero in args: 
    try:
      resultado=+numero 
      print(resultado)
    except:
      print("Imposible")
print(error("2",10))