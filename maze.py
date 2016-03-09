import random
import math

"""dhmiourgia pinaka 10x10"""
table=[[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],
       [2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[2,9],[2,10],
       [3,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],[3,9],[3,10],
       [4,1],[4,2],[4,3],[4,4],[4,5],[4,6],[4,7],[4,8],[4,9],[4,10],
       [5,1],[5,2],[5,3],[5,4],[5,5],[5,6],[5,7],[5,8],[5,9],[5,10],
       [6,1],[6,2],[6,3],[6,4],[6,5],[6,6],[6,7],[6,8],[6,9],[6,10],
       [7,1],[7,2],[7,3],[7,4],[7,5],[7,6],[7,7],[7,8],[7,9],[7,10],
       [8,1],[8,2],[8,3],[8,4],[8,5],[8,6],[8,7],[8,8],[8,9],[8,10],
       [9,1],[9,2],[9,3],[9,4],[9,5],[9,6],[9,7],[9,8],[9,9],[9,10],
       [10,1],[10,2],[10,3],[10,4],[10,5],[10,6],[10,7],[10,8],[10,9],[10,10]]
       
"""apodosh tuxaias theshs ston paikth kai ston thudsauro"""
paikths=random.choice(table)
thusavros=random.choice(table)
print paikths
print thusavros

"""upologismos apostashs paikth-thusaurou"""
x1=paikths[0]
y1=paikths[1]
x2=thusavros[0]
y2=thusavros[1]
apostash=math.fabs(x2-x1)+ math.fabs(y2-y1)
print apostash

"""kinhsh paikth"""
while (apostash>0):
	move=raw_input("Metaknhsou:")
	if (move=="w"):
		if (paikths[0]!=1):
			paikths[0]=paikths[0]-1
		else:
			print "Toixos"
	elif (move=="s"):
		if (paikths[0]!=10):
			paikths[0]=paikths[0]+1
		else:
			print "Toixos"
	elif (move=="a"):
		if (paikths[1]!=1):
			paikths[1]=paikths[1]-1
		else:
			print "Toixos"
	elif (move=="d"):
		if (paikths[1]!=10):
			paikths[1]=paikths[1]+1
		else:
			print "Toixos"
	else:
		print "Lathos plhktro,pata ena apo: w,a,s,d"
	x1=paikths[0]
	y1=paikths[1]
	x2=thusavros[0]
	y2=thusavros[1]
	apostash=math.fabs(x2-x1)+ math.fabs(y2-y1)
	print apostash

print "Bravo vrhkes ton thusavro"
