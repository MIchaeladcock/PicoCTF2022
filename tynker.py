cypher = [350,372,192,354,139,337,67,311,392,338,241,414,180,277,379,294,128,117,250,404,336,350,386]
#cypher = [350] #19V3R5

characters = ['A','B','C','D','E','F','G','H','I','J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0','1','2','3','4','5','6','7','8','9','_']
#numbers = 	 ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25',26   27  28  29  30  31  32  33  34  35  36  37]

solve = ['28','36','22','30','18','32','30','12','25','37','8','31','18','4','37','6','33','34','31','34','36','28','29']
solve2 = [28,36,22,30,18,32,30,12,25,37,8,31,18,4,37,6,33,34,31,34,36,28,29]

#print(solve2)

for x in cypher:
#	print(x)
	for j in x:
		print(j)
#	characters[(j)]

"""
def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
 
    if (m == 1):
        return 0
 
    while (a > 1):
 
        # q is quotient
        q = a // m
 
        t = m
 
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t
 
    # Make x positive
    if (x < 0):
        x = x + m0
 
    return x
 """
 
#### Driver code
#a = 350 #5
#m = 41 #350 % 41
 
#### Function call
#print(modInverse(a, m))


	
#	decode = x % 41
#	print(decode)
#	print(characters[decode])
#	res = pow(5, 350-1, 350)
#	print(res)