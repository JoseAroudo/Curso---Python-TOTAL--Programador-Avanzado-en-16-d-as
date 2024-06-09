def Ceros(*args):
    ind=0
    for i in args:
        if i==0:
            ind += 1
            if ind==2:
                print("hola")
                return True

            else:continue
        else:
            ind= 0
        continue
    print("adios")
    return False


Ceros(2,7,3,0,5,0,1,0,0)