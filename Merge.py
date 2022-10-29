import Convertmodules as zhmk
def hb():
    version = 1.0
    print("\033[31m[Console]:\033[0m","Merge库版本为", version)
    a = zhmk.zh("export/ip.txt")
    b = zhmk.zh("export/port.txt")
    d = open("export/combo.txt","w")
    i = 0
    print("\033[31m[Console]:\033[0m","开始合并IP与Port")
    try:
        while True:
            c = a[i]+":"+b[i]+"\n"
            i += 1
            d.write(c)
    except Exception as e:
        pass