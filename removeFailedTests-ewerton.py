from glob import glob
import os

files = glob('./**/Result.csv', recursive=True)

for i in files:
  file = open(i,'r')
  contents = file.read()

  if 'Failed' in contents:
    file.close()
    path = i[:-11] # remove '\Result.csv'
    print('Failed test in directory:', path)
    command = "rmdir " + path + " /s"
    os.system(command)
  else:
    file.close()



