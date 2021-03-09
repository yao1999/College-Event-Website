

email = "zefeng.yao@knights.ucf.edu"

domain = email.split('@')[1].split('.')
if domain.count('ucf'):
    print("yes")
else:
    print("no")
  
