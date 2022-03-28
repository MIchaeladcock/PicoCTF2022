cypher = [128,63,131,198,262,110,309,73,276,285,316,161,151,73,219,150,145,217,103,226,41,255]


characters = ['A','B','C','D','E','F','G','H','I','J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0','1','2','3','4','5','6','7','8','9','_']
#numbers = 	 ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25',26  27  28  29  30  31  32  33  34  35]

mod37 = []
for x in cypher:
	mod37 = x % 37
	print (characters[mod37])



"""
num = 1
print(characters[:num])

input = 'a'
#input = input.lower()
output = []
for character in input:
    number = ord(character) - 96
    output.append(number)
#print (output)

#for x in output:
#	print(chr(ord('@') + x ))
"""