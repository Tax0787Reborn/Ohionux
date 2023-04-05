try:
    from os import system as s
    from os import chdir as c
    from os import getcwd as g
    from os.path import join as j
    import sys
    b,gs=1,g()
    def core(a):
        global b
        if 'cd' in a:c(a.split(' ')[1].replace('\\_',' '))
        elif a=='%quit%':b=0
        elif a=='0spy_shell':s(j(gs,'0spy_shell.py'))
        elif a=='edit':s(j(gs,'edit.py'))
        else:s(a)
    def shells():
        global b
        print("BZ3's ohionux oshell is started")
        while b:
            a=input(': >[ BZ3 ]>')
            core(a)
        print("BZ3's ohionux oshell is ended")
    def file_exec():
        global b
        for _ in open(sys.argv[1],encoding="utf-8").read().split('\n'):
            core(_)
            if not b:break
    if __name__=="__main__":
        if len(sys.argv)==1:shells()
        else:file_exec()
except Exception as error:
    print('ERROR')
    print('type :',type(error),'what? :',error)
