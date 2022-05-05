import sys
import os
import os.path
import glob
import shutil

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


    
    

# https://stackoverflow.com/questions/5622976/how-do-you-calculate-program-run-time-in-python
# https://www.delftstack.com/howto/python/python-run-another-python-script/

'''
folder = Ознакомительная папка
path = "Users/mihail/Documents/proj/op/tasks for D4"
'''
createAndCopy("tasks A B", "Ознакомительная папка")


#createCatalog("tasks A B", "Ознакомительная папка/Тема А")
#createCatalog("tasks A B", "Ознакомительная папка/Тема Б")



'''
os.mkdir("Users/mihail/Documents/proj/op/ tasks for D4")

'''
'''
filenames = glob.glob(os.path.join(src_path, "task_A*.py"))
    for filename in filenames:
        if os.path.isfile(filename):
            shutil.copy2(filename, task_A_path)

    filenames = glob.glob(os.path.join(src_path, "task_B*.py"))
    for filename in filenames:
        if os.path.isfile(filename):
            shutil.copy2(filename, task_B_path)
'''


