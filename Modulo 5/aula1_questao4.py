from datetime import date
from datetime import datetime #importa da biblioteca datetime
data = date.today() #lê a data atual
data2 = data.strftime('%d/%m/%Y') #reformula a data atual
hora = datetime.now().time() #Lê a hora atual
hora2 = hora.strftime('%H:%M') #Reformula a hora atual
print(f"Data: {data2}") #imprime a data atual
print(f"Hora: {hora2}")