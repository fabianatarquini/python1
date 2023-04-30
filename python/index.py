import random

#João está em uma sala onde existem duas portas sem nenhuma identificação, uma delas leva à vitória e a outra à derrota. 

# Na sala também existem dois computadores, um deles está programado para responder apenas com a verdade e o outro apenas com a mentira, mas João não sabe qual é qual.

# João pode fazer uma única pergunta a um dos computadores. Elabore uma pergunta que João poderia fazer e qual o procedimento ele deve tomar, em função da resposta recebida, para sair pela porta vitoriosa?


import random
import numpy as np

n_aleatorio=random.randint(0,1)

#precisa escolher o computador

escolha_porta=int(input("Entre com 1 para porta 1 ou 2 para a porta 2: "))

Q= input( "faça sua pergunta de modo que a resposta seja verdadeiro ou falso: ")
Q= eval(Q)

if n_aleatorio==0:
    if escolha_porta==1:
        r1= Q
        print("A resposta é: ",r1)
    if escolha_porta==2:
        r2=not Q
        print("A resposta é: ",r2)

if n_aleatorio==1:
    if escolha_porta==1:
        r1= not Q
        print("A resposta é: ",r1)
    if escolha_porta==2:
        r2= Q
        print("A resposta é: ",r2)


print("Agora, escolha a porta Vencedora!")

n_final=int(input("Digite 1 para entrar na porta 1 ou digite 2 para entrar na porta 2: "))

if n_aleatorio==0 and n_final==1:
    print("Parabéns você ganhou, vitória!")
    
if n_aleatorio==0 and n_final==2:
    print("Você perdeu,derrota!")


if n_aleatorio==1 and n_final==1:
    print("Você perdeu,derrota!")
    
if n_aleatorio==1 and n_final==2:
    print("Parabéns você ganhou, vitória!")






