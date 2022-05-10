from datetime import datetime
import sys
import os
import os.path
import glob
import shutil
import timeit
import re
import subprocess

def copyFiles(src_path, fileMask, dst_path):
    filenames = glob.glob(os.path.join(src_path, fileMask))
    for filename in filenames:
        if os.path.isfile(filename):
            shutil.copy2(filename, dst_path)
            
def createAndCopy(src_path, dst_path):
    os.makedirs(dst_path, exist_ok=True)
    task_A_path = os.path.join(dst_path, "Тема А")
    os.makedirs(task_A_path, exist_ok=True)
    task_B_path = os.path.join(dst_path, "Тема Б")
    os.makedirs(task_B_path, exist_ok=True)
    copyFiles(src_path, "task_A*.py", task_A_path)
    copyFiles(src_path, "task_B*.py", task_B_path)
    
def FileReading(q):
    FUNCTION_REGEX = r'(?<=def\s)(.*)(?=:)'
    p = os.path.abspath('Ознакомительная папка')
    for fold in os.listdir(p):
        s = os.path.join(p, fold)
        files = glob.glob(os.path.join(s,"task_*.py"))
        folderName = os.path.basename(fold)
        print('folder', "\"" ,folderName, "\"")
        for file in files:
            start = timeit.default_timer()
            name = os.path.basename(file)
            print('\tscript "{0}"'.format(name.strip()))
            with open(file) as f:
                task = f.read()
            funcs = re.findall(FUNCTION_REGEX, task, re.MULTILINE)
            for func in funcs:
                print('\t\tfunction "{0}"'.format(func.strip()))   
            result = subprocess.Popen(['python',file], stdout=subprocess.PIPE)
            out, err = result.communicate()
            print('\t\toutput "{0}"'.format(out.decode('UTF-8').strip()))
            stop = timeit.default_timer()
            time = stop - start
            print('\t\ttime "{:.3f} sec"'.format(time))

createAndCopy("tasks A B", "Ознакомительная папка")
FileReading(1)


