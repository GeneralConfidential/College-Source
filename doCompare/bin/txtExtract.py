import os

os.chdir('..')
os.chdir('chkFiles/')

file1 = open('doc1.txt','r')
file2 = open('doc2.txt','r')

txt1 = file1.read()
txt2 = file2.read()