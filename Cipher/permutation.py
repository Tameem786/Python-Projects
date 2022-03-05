
# Python code to demonstrate 
# to find all permutation of
# a given string
  
# Initialising string
ini_str = "u3c0n7h0l0n__7r_jmp"
prefix = "XCTF21{"
suffix = "}"
  
# Printing initial string
print("Initial string", ini_str)
  
# Finding all permuatation
result = []
  
def permute(data, i, length): 
    if i == length:
        s = ''
        print(s.join(data))
            #result.append(''.join(data) )
    else: 
        for j in range(i, length): 
            # swap
            data[i], data[j] = data[j], data[i] 
            permute(data, i + 1, length) 
            data[i], data[j] = data[j], data[i]  
permute(list(ini_str), 0, len(ini_str))
  
# Printing result
#print(result)