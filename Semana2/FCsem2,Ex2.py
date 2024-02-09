# Angelo Del Rey 
# Aula 2 Física computacional: sistema massa mola

palavra = ""
meta = "Fisica" 

for i in range(len(meta)*2): 
    if i<len(meta):
        palavra = palavra + meta[i]
        print(palavra)
    else:
        palavra = palavra[:-1]
        print(palavra)

