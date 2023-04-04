vetorPossibilidade = [True, False]
print('testando de formulas tabajara 1.0')
print("(A ^ B) v (¬A^ ¬B)")
for a in vetorPossibilidade:
    for b in vetorPossibilidade:
         if (a and b) or (not a and not b): # not a = ¬a 
              resultadoF=True
         else:
              resultadoF=False
         print(f'A = {a} \t B = {b} \t formula={resultadoF}') # \t pra deichar o testo alinhado 
          
print('(A == B)^ ¨¬(A v B)')
for a in vetorPossibilidade:
    for b in vetorPossibilidade:
         if (a == b) and not(a or b): # not a = ¬a 
              resultadoF=True
         else:
              resultadoF=False
         print(f'A = {a} \t B = {b} \t formula={resultadoF}') # \t pra deichar o testo alinhado 


         