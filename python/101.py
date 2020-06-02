import re

ex = r'^([1]{1}[0]{1}[1]{1})$'
res = re.compile(ex)
prueba = raw_input("entrada: ")
busqueda=re.search(res,prueba)

if busqueda:
    print busqueda.group()
else:
    print"qr"
