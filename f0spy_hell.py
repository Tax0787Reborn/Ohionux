try:
    from os import remove as rf
    from os import rmdir as rd
    from os import mkdir as md
    from os import listdir as ld
    from os.path import splitext as st
    import sys
    links,o={},open
    read=lambda f:o(f,encoding='utf-8').read()
    write=lambda f,s:o(f,'w',encoding='utf-8').write(s)
    copy=lambda f,f2:write(f2,read(f))
    def move(f,f2):
        a=copy(f,f2)
        b=rf(f)
        return(a,b)
    def link(f):
        global links
        links[f]=read(f)
    def helps():
        print('''
        rf : remove file
        rd : remove directory
        md : make directory
        ld : look (list) directory
        read : read text file
        write : write text file
        copy : make clone of any text file
        move : move files
        link : activation the ohio-link (*.tol)
        help : help you LoL, kek
        ''')
    def tuples(argvs):
        if isinstance(argvs,list) and argvs:
            a=argvs[0]
            for _ in argvs[1:]:a+=','+_
            return a
        elif isinstance(argvs,list):
            return ''
        else:
            return str(argvs)            
    def shells():
        print("BZ3's Ohionux is started")
        while 1:
            a=core(input("0ω0 : "))
            if a=='exit()':break
            else:exec(a)
        print("BZ3's Ohionux is ended")

    def core(a2):
        a=a2
        global links
        for i,j in links.items():
            a=a.replace(i,j)
        if a=='$exit$':c='exit()'
        else:
            b=a.split('>ω<')
            c='a='+b[0]+'('+tuples(b[1:])+')\nprint(a)'
        return c
    def file_compile():
        a=''
        for _ in read(sys.argv[1]).split('\n'):
            a+=core(_)+'\n'
        return a
    def file_exec():
        for _ in file_compile().split('\n'):
            exec(_)
    if __name__=="__main__":
        if len(sys.argv)==1:shells()
        else:
            if len(sys.argv)==3:
                if sys.argv[2]=='--compile':open(st(sys.argv[1])[0]+'.py','w').write('''from os import remove as rf
from os import rmdir as rd
from os import mkdir as md
from os import listdir as ld
links,o={},open
read=lambda f:o(f).read()
write=lambda f,s:o(f,'w').write(s)
copy=lambda f,f2:write(f2,read(f))
def move(f,f2):
    a=copy(f,f2)
    b=rf(f)
    return(a,b)
def link(f):
    global links
    links[f]=read(f)
def helps():
    print("""
    rf : remove file
    rd : remove directory
    md : make directory
    ls : look (list) directory
    read : read text file
    write : write text file
    copy : make clone of any text file
    move : move files
    link : activation the ohio-link (*.tol)
    help : help you LoL, kek
    """)
'''+file_compile())
                elif sys.argv[2]=='--exec':file_exec()
            else:file_exec()
except Exception as error:
    print('ERROR')
    print('type :',type(error),'what? :',error)
