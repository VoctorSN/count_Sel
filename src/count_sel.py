def count_sel(lst):
    once_values=0
    appeared=[]
    max_ocurrance=0
    nb_max_ocurrance=[]
    for num in lst:
        if num in appeared:
            continue
        else:
            numeros_aparecidos.append(num)
        if lst.count(num)>max_ocurrance:
            max_ocurrance=lst.count(num)
            nb_max_ocurrance=[num]
        if lst.count(num)==max_ocurrance and num not in nb_max_ocurrance:
            nb_max_ocurrance.append(num)
        if lst.count(num)==1:
            once_values+=1
    nb_max_ocurrance.sort()
    return [len(lst),len(numeros_aparecidos),once_values,[nb_max_ocurrance,max_ocurrance]]
