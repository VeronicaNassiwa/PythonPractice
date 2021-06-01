
class person :
    def __init__(access,Fname,Lname):
        access.Fname=Fname
        access.Lname=Lname

prsn = person("Nassiwa","Veronica")

#print(prsn.Fname)
#print(prsn.Lname)

#This can also print the same results

class Student :
    def __init__(names):
        names.Frstname="Nasrah"
        names.Lstname="Nassiwa"
        names.ave=[2,3,4,5,6,7]
        names.avera=sum(names.ave)/len(names.ave)

stdt = Student()
print(stdt.Frstname)
print(stdt.Lstname)
print( "The average is {}" .format(stdt.avera) )

