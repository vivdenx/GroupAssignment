# Get dataset with only Athletes.
list_athletes=[]
filename = '' 
with open(filename) as file:
    for line in file:
        if 'athlete' in line$occupation:
            dict_athelete={}
            dict_athelete['name']=line['name']
            dict_athelete['sport']=line['sport']
            dict_athelete['sign']=line['sign']
            dict_athelete['sex']=line['sex']
            dict_athelete['country']=line['country']
            dict_athelete['occupation']=line['occupation']
            dict_athelete['date_of_birth']=line['date_of_brith'] 
            list_athletes.append(dict_athelete)

print(list_athletes)

