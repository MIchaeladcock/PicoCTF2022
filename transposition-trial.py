#!/bin/env python3

cypher = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_VCDE4CE4}7"

## makes a list from the cypher text
removedCypherChars = list(cypher)

## Removes every 3rd char from Cypher
del removedCypherChars[2::3]



## makes a list from cypher with only evey 3rd chr
cypherChars = list(cypher[2::3])


## Turns the list in iterators
addTheseLetters = iter(cypherChars)
removedChars = iter(removedCypherChars)


new_list = []

try:
    while True:
        if len(new_list) % 3 == 2 or len(new_list) == 0:

            new_list.append(next(addTheseLetters))
            new_list.append(next(removedChars ))
            new_list.append(next(removedChars ))
            #print(new_list)
            #print('if')

        else:
            new_list.append(next(addTheseLetters))
            new_list.append(next(removedChars))
            new_list.append(next(removedChars))
            #print(new_list)
            #print('else')

except StopIteration:
    pass

print (''.join(new_list))

