salario_atual = float(input())
salario_min = float(input())

if salario_atual <= salario_min*3:
    if salario_atual < salario_min*1.5:
        salario_atual = salario_min*1.5
        reajuste = 0
    else:
        reajuste = salario_atual*0.2

elif salario_atual > salario_min*3 and salario_atual <= salario_min*5:
    reajuste = salario_atual*0.15
    
elif salario_atual > salario_min*5:
    reajuste = salario_atual*0.1
    if reajuste+salario_atual > salario_min*20:   
        reajuste = salario_min*20 - salario_atual 
        
    
print(salario_atual+reajuste)