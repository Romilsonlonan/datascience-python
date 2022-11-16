# Listas de listas são matrizes em python 

listas = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]
listas = [] 
  
for i in range(5): 
      
    
    listas.append([]) 
      
    for j in range(5): 
        listas[i].append(j) 
          
print(listas)