import os
#print(os.getcwd)
file_name = input("Enter the file name")
paths = ("/home")
result=[]
os.chdir(paths)
#location =
#print(os.getcwd())
for root,dirs,files in os.walk(paths):
    if file_name in files:
        result.append(os.path.join(root,file_name))



loc = str(result)
loc = loc.replace('[','')
loc = loc.replace(']','')
loc = loc.replace("'","")
print(loc)
#os.remove(loc)
#print(type(loc))
try:
    os.remove(loc)
    print("Deleted Successful")
except:
    print("No such file")




'''
try:
    print(os.remove(file_name))
except:
    print("error")

'''
'''d = path("home/")
num_files = len(d.files())
print(num_files)
'''
