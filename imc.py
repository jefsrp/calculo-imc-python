# Calculadora de IMC

nome = input('Qual seu nome?')
peso = float(input('Qual seu peso?'))
altura = float(input('Qual sua altura?'))

# Caulculo do IMC

imc = peso / (altura **2)

# Classificação do IMC

if imc < 18.5:
     Classificação =" Abaixo do peso "   

elif imc < 25:
        Classificação = " Peso normal "

elif imc < 30:
        Classificação = " Sobrepeso"   

elif imc < 35:
        Classificação = " Obesidade grau 1" 

elif imc < 40:
        Classificação = " Obesidade grau 2" 

else :
        Classificação = "Obesidade Grau 3"

 # Resultado IMC       
   
print(f'{nome}, seu IMC é {imc:.2f}')  
print(f'Classificação: {Classificação}')

print('Obrigado por utilizar meu programa de calculo IMC. Ate logo!')  
   
