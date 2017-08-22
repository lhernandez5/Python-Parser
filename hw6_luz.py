#!/usr/bin/python3/


with open('hw5.vcf','r') as infile, open('hw6.out', 'w') as outfile:
    outfile.write('ID\t\tREF\tALT\tRAF\n')
    for line in infile.readlines():
        if line.startswith('#'):
            continue
        elif line.startswith('\n'):
            continue

        else:
            line = line.strip()
            col = line.split('\t')
            col[0:1]
            genotype = col[9:]
            alleles = []
            for g in genotype:
                alleles.append(g.split(':')[0])
            alleles_out = '\t'.join(alleles)
            list=[]
            def function(list, alleles):
                T= list.count(0)
                N=(2.0*(len(alleles)))
                return ((T)/(N))
            for x in alleles:
                if x=='0|0':
                    list.append(0)
                    list.append(0)
                elif x=='1|0' or x=='0|1':
                    list.append(0)
                elif x=='1|1':
                    list.append(1)
            myinfo = [col[2], col[3], col[4]]
            myout = '\t'.join(myinfo)
            outfile.write(myout + '\t' + str(function(list, alleles)) + '\n')
        
    print("\nCongrats your vcf file was processed!\n")
