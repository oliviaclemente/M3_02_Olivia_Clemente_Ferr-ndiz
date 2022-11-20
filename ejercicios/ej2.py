lista=[4, 7, 30, 23, 5]
def error(lista):
  try:
    lista[10]
  except:
    print("Error")
print(error(lista))