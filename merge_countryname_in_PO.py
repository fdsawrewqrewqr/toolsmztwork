mawfile=open('maw.po','r')
mawfiletmp=open('mawtmp.po','w')

m=mawfile.readlines()

arabic=open('arabic.po','r')
arabictmp=open('arabictmp.po','w')

a=arabic.readlines()

ir=-1
for arabicline in a:
	ir = ir + 1
	if arabicline.find('msgid') != -1:
		try:
			id=m.index(arabicline)			
			m[id+1] = a[ir+1] 
		except ValueError:
			arabictmp.write(arabicline)
			arabictmp.write(a[ir+1])
			arabictmp.write('\n')			
	else:
		continue
			
mawfiletmp.writelines(m)



mawfile.close()

mawfiletmp.close()

arabic.close()
arabictmp.close()

