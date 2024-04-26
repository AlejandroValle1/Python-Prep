class Herramientas:
    def __init__(self, lista_numeros):
             self.lista = lista_numeros

    def verifica_primo(self):
        for i in self.lista:
            if (self.__verifica_primo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo') 

    def convertidor_grados(self, origen, destino):
       for i in self.lista:
          print(f"{i} grados son {self.__convertidor_grados(i,origen,destino)} {origen}")

    def factorial(self):
       for i in self.lista:
          print("El factorial de",i, "es",self.__factorial(i))
        
    def __verifica_primo (self, numero):
        es_primo = True
        for i in range(2,numero):
         if numero % i ==0:
          es_primo = False
        return es_primo

    def numero_repetido(self,menor ):
      lista_unicos=[]
      lista_repetidos=[]
      if len(self.lista) == 0:
         return None
      for elemento in self.lista:
        if elemento in lista_unicos:
            i= lista_unicos.index(elemento)
            lista_repetidos[i] += 1
        else:
            lista_unicos.append(elemento)
            lista_repetidos.append(1)
            numero_rep= lista_unicos[0]
            cantidad_rep= lista_repetidos[0]
      for i, elemento in enumerate(lista_unicos):
        if lista_repetidos[i] > cantidad_rep:
            numero_rep= lista_unicos[i]
            cantidad_rep= lista_repetidos [i]
            return numero_rep, cantidad_rep
    
    def __convertidor_grados(self, valor, medida_origen, medida_destino):
      if medida_origen == "celsius":
        if medida_destino == "celsius":
            valor_final= valor
        elif medida_destino == "farenheit":
            valor_final = (valor * 9/5) + 32
        elif medida_destino == "kelvin":
            valor_final =valor + 273.15 
        else: 
            print ("Parametro incorrecto")
      if medida_origen == "farenheit":
        if medida_destino == "farenheit":
            valor_final = valor
        elif medida_destino == "celsius":
            valor_final = (valor - 32) * 9/5
        elif medida_destino == "kelvin":
            valor_final= (valor - 32 * 9/5) + 273.15
        else:
            print ("Parametro incorrecto")
      if medida_origen == "kelvin":
        if medida_destino== "kelvin":
            valor_final= valor
        elif medida_destino == "celsius":
            valor_final= valor - 273.15
        elif medida_destino == "farenheit":
            valor_final= (valor - 273.15 * 9/ 5 ) + 32
        else:
            print ("Parametro incorrecto")
            
      return valor_final

    def __factorial(self, numero):
      if type(numero) != int:
        return "El número no es un entero"
      if numero < 0:
        return "El numero no es positivo"
      if numero <= 1:
        return 1
      numero = numero * self.__factorial(numero - 1)
      return numero