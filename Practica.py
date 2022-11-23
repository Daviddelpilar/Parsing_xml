# muestra la descripción de todos los productos por consola. No solo de uno.
# archivo xml de referencia en el siguiente enlace
# Al Café negro le añadimos el precio 9.95

from bs4 import BeautifulSoup
print('Practica en python')

with open ('Productos.xml','r') as f:
    data=f.read()
print(data)

Bs_data=BeautifulSoup(data,'xml')
print(Bs_data)

descripciones=Bs_data.find_all('Productos')
print(descripciones)


for tag in Bs_data.find_all('Producto', {'ID':'100001'}):
    tag['Precio'] = "9.95"
print(Bs_data.prettify())
