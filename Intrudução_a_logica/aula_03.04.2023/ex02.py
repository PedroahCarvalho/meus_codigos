print('(A == B)^ ¨¬(A v B)')
for a in vetorPossibilidade:
    for b in vetorPossibilidade:
         if (a == B) and not(a or b): # not a = ¬a 
              resultadoF=True
         else:
              resultadoF=False
         print(f'A = {a} \t B = {b} \t formula={resultadoF}') # \t pra deichar o testo alinhado 
         