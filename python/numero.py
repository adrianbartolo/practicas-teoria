import re

ex = r'^([0]{1}[1]{1}[0]{1})$'
resultado = re.compile(ex)
prueba = raw_input("entrada: ")
busqueda=re.search(resultado,prueba)

if busqueda:
    print busqueda.group()
else:
    print"qr"
