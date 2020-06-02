import re

ex = r'^([a-z]{3,5})$'
resultado = re.compile(ex)
prueba = raw_input("entrada: ")
busqueda=re.search(resultado,prueba)

if busqueda:
    print busqueda.group()
else:
    print"qr"
