import sys

header="""<html lang="en"> <head> <meta charset="UTF-8"> <title>mor's website</title> </head> """

colors = ['blue', 'red', 'green']
n = raw_input("enter n value:\n")

body="<body> "

col_width=100/int(n)

for i in range(0,int(n)):
    body+='<div style="height: 100%; width: ' + col_width.__str__() + '%; background-color: ' + colors[i%colors.__len__()] + '; float:left"></div> '

body+='</body>'

footer='</html>'

f = open("foo4.html","w+")

f.write(header)
f.write(body)
f.write(footer)
f.close()
