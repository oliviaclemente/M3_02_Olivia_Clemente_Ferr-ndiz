paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
def error(paises):
  try:
    paises["alemania"]
  except:
    print("Error")

print(error(paises))