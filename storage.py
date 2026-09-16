def load_s():
    slist=[]
    try:
        f=open("students.txt", "r")
        for line in f:
            line = line.strip()
            data = line.split(",")
            slist.append(data)
        f.close()
    except FileNotFoundError:
        pass
    return slist

def save(r,n,c):
    f=open("students.txt", "a")
    f.write(r+','+ n+','+ c+ '\n')
    f.close()
    
def load_a():
    alist=[]
    try:
        f =open("attendance.txt", "r")
        for l in f:
            l = l.strip()
            data = l.split(",")
            alist.append(data)
        f.close()
    except FileNotFoundError:
        pass
    return alist

def asave(r,date,status):
    f = open("attendance.txt", "a")
    f.write(r + "," +date + "," +status +"\n")
    f.close()



