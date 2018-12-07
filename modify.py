import os

file = open('abstract10000.json','r')
content = file.read()
file.close()
os.remove("abstract.json")

fixed_content = content[11:-2]
fixed_content = fixed_content.replace('},{','}\n{')
#for line in fixed_content:
#	print line
#	x = raw_input("test")
fixed_file = open('modified_abstract.json','w')
fixed_file.write(fixed_content)
