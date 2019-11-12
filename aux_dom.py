#coding:utf-8

def get_cod_from_geom(geom):
	l_cod = []
	geom = geom[0].split(',')
	for line in geom:
		line = line.split('\n')[0]
		if ('CD_GEOCODI' in line):
			cod = line.split(':')[-1].split('\"')[1]
			l_cod.append(cod)
	return l_cod

def get_num_h_num_m(l_cod, dom):
	res = {}
	for line in dom:
		line = line.split('\n')[0]
		num_h = 0
		num_m = 0
		line = line.split(';')
		cod = line[0]
		print(cod)
		if (line[0] not in l_cod): continue
		for i in range(63, 82):
			num_h += int(line[i])
		for i in range(82, 101):
			num_m += int(line[i])
		if (num_h > num_m):
			res[cod] = 'Homens'
		elif (num_h < num_m):
			res[cod] = 'Mulheres'
		else:
			res[cod] = 'Igual'
	return res
		

# homens responsáveis: v062 - v080
# mulheres responsáveis: v081 - v099
geom = 'topojson/mcz.json'
dom = 'domicilio-mcz.csv'
out = 'domicilio_sb.csv'

out = open(out, 'w')

geom = open(geom)
geom = geom.readlines()

dom = open(dom)
dom = dom.readlines()

l_cod = get_cod_from_geom(geom)

res = get_num_h_num_m(l_cod, dom)

out.write('Cod_setor,maior_parte\n')
for cod in res:
	print(cod)
	out.write('%s,%s\n' % (cod, res[cod]))
out.close()