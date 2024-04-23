def notas(* resp,sit=False):
    num = dict()
    num['Total'] = len(resp)
    num['Maxima'] = max(resp)
    num['Minimo'] = min(resp)
    media = sum(resp) / len(resp)
    num['Media'] = media

    if sit==True:
        if media >= 7:
            num['sit'] = 'boa'
        if media >= 6 and media < 7:
            num['sit'] = 'marromeno'
        if media < 6:
            num['sit'] = 'horrivel'
    return num    
    

#Programa Principal
resp = notas(5.5, 9.5, 10, 6.5,sit=True)
print(resp)
