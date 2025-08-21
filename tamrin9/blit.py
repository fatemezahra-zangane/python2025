sen=int(input("sen ra vared kon"))
daneshamoz=int(input("aya danesh amozi?(yes or no)"))
if sen<12 and daneshamoz=="yes":
    print("5000 toman")
    if 12<sen<18 and daneshamoz=="yes":
        print("10000 toman")
    else :
        print("20000toman")
