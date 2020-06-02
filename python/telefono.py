import re

ex = r'(712)(\-)([0-9]{3})(\-)([0-9]{4})'
resultado = re.compile(ex)
prueba = raw_input("entrada: ")
busqueda=re.search(resultado,prueba)
if busqueda:
    print busqueda.group()
else:
    print"qr"

