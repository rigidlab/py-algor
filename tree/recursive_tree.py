#Recursive programs to write to data.json tree structure given:
#Nodes: List of node names
#Childnodes: List of childnodes of each node. Child nodes may be a subset of nodes
fixednodes=['language','culture','speaking','reading','food','drink']
childnodes=[['speaking','reading'],['food','drink'],[],[],[],[]]
dbf=open('data.json','w')
i=1
dbf.write("{\n")
dbf.write('\"name\":\"Root\",\n')
dbf.write('\"children\":[\n')
def rec_expand(nodes,childnodes):
	global i
	if len(nodes)!=0:
		for pi in nodes[:-1]:
			dbf.write("  "*i+"{\n")
			dbf.write("  "*i+'\"name\":'+'\"'+str(pi)+'\"')
			if len(childnodes[fixednodes.index(pi)])!=0:
				dbf.write(','+'\n')
				dbf.write('  '*i+'\"children\":\n')
				dbf.write('  '*i+'[\n')
				i+=1
				rec_expand(childnodes[fixednodes.index(pi)],childnodes)
				i+=-1
				dbf.write('  '*i+']\n')
			else:
				dbf.write('\n')
			dbf.write("  "*i+"},\n")
		dbf.write("  "*i+"{\n")
		dbf.write("  "*i+'\"name\":'+'\"'+str(nodes[-1])+'\"'+'\n')
		dbf.write("  "*i+"}\n")

rec_expand(fixednodes,childnodes)
dbf.write(']\n')
dbf.write("}\n")
dbf.close()