ficha = list()
for nome in range(100):
    matricula = int(input("digite sua matricula"))
    nota = int(input("digite sua nota"))
    nota5=[]
    

    if nota > 5:
        nota5.append(nota)
        
    ficha.append([nota, matricula])
    ficha.sort()
    porc5 = (len(nota5) / 100) * 100
    
maior = ficha[-1][-2]
alunmaior = ficha[-1][-1]
segmaior = ficha[-2][-2]
alunseg = ficha[-2][-1]
    
print('-=' * 30)
print("a porcentagem de alunos que tiraram acima de 5 foi:",porc5, "%")
print('-=' * 30)
print("a maior nota foi", maior, "do aluno", alunmaior)
print('-=' * 30)
print("a segunda maior nota foi", segmaior, "do aluno",alunseg)