from os import chdir
import sys
import timeit, dis
import subprocess, marshal, py_compile
import numpy as np
import pandas as pd
from tempfile import NamedTemporaryFile
from collections import defaultdict
from os.path import exists

from pandas.core.indexes.base import Index

def task1():
    if len(sys.argv)<= 2:
        print("[ERROR] : Put more args")
        return

    results = dict()
    for i in sys.argv[1:]:
        if not exists(i):
            print(f"File {i} does not exist")
        else:
            timer = timeit.timeit(lambda : subprocess.run (["python3",i], stdout=subprocess.PIPE), number=1)
            results[i] = timer
            print(f"File {i} does exist")
    print(results)
    row_format = "{:<16}| {:<6}| {: <16}"
    j=0
    print(row_format.format("PROGRAM","RANK","TIME"))
    for k, v in sorted(results.items(), key = lambda item : item[1]):
        print(row_format.format(k, j, v))
        j += 1

def get_bytecode(arg):
    return dis.Bytecode(arg)

def expand_bytecode(bytecode):
    res=[]
    for instruction in bytecode:
        if str(type(instruction.argval)) == "<class 'code'>":
            res += expand_bytecode(dis.Bytecode(instruction.argval))
        else:
             res.append(instruction)
    return res

def print_bc():
    for i in sys.argv[3:]:
        source = None
        if sys.argv[2] == "-py":
            try:
                with open(i,"r") as f:
                    source = f.read()
            except Exception as e:
                print(f"Skipping : {i}")
        elif sys.argv[2] == "-pyc":
            try:
                header = 12
                if sys.version_info >=(3,7):
                    header = 16
                with open(i, "rb") as target:
                    target.seek(header)
                    source = marshal.load(target)
            except Exception as e:
                print(f"Skipping : {i}")
        elif sys.argv[2] == "-s":
            source=i
        else:
            print("ERROR!")
            return
        bc = get_bytecode(source)
        instructions = expand_bytecode(bc)
        for instruction in instructions:
            print(f"{instruction.opname}\t {instruction.argrepr}")


def compile():
    for i in sys.argv[3:]:
        if sys.argv[2]=="-py":
            try:
                py_compile.compile(i, cfile= i + "c")
            except Exception as e:
                print(f"We skipping {i}")
                
        elif sys.argv[2] == "-pyc":
            pass
        elif sys.argv[2] == "-s":
            with NamedTemporaryFile("w",delete = True) as tmp:
                tmp.write(i)
                tmp.seek(0)
                py_compile.compile(tmp.name, cfile="task4_output_s.pyc")
        else:
            print("Error")
            return
    
def compare():
    instList = []
    d={}

    for i in range(0, len(sys.argv)):
        D = {}
        source = None

        if sys.argv[i]=="-py":
            with open(sys.argv[i+1],'r') as f:
                source = f.read()
                

        elif sys.argv[i] == "-pyc":
            header_size = 12
            if sys.version_info >= (3,7):
                header_size = 16
            with open(sys.argv[i+1],'rb') as f:
                f.seek(header_size)
                source = marshal.load(f)
        elif sys.argv[i] == "-s":
            source = sys.argv[i+1]
        else:
            continue

        bc = get_bytecode(source)
        Instructions = expand_bytecode(bc)
        
        for instruction in Instructions:
            if instruction.opname in D:
                D[instruction.opname]+=1
                instList.append(instruction.opname)
            else:
                D[instruction.opname]=1
                
        d[sys.argv[i+1]] = D 


        instList = list(np.unique(instList))

        for v in d:
            j = d[v]

            for inst in instList:
                if inst in j:
                    pass
                else:
                    d[v][inst]=0
                
            
    df = pd.DataFrame(d)
    df = df.fillna(0)
    #df.index.name='INSTRUCTIONS'
    df.columns = df.columns.map(lambda x : " |  " + x)

    print(df.to_string(index=True,header=True))
    
        



if __name__ == '__main__':
    if len (sys.argv)==1:
        print("NO ACTION!") 
    
    else:
        if sys.argv[1]=="task1":
            task1()
        #elif sys.argv[1]=="c":
        #    py_compile.compile("src1.py", cfile="src1.pyc")
        elif sys.argv[1]=="print":
            print_bc()
        elif sys.argv[1]=="compile":
            compile()
        elif sys.argv[1]=="compare":
            compare()