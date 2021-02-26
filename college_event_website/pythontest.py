
# this is for me to test if the python code is right or not
# I'll delete this when we submit this

def check_input(inputs):
  for input in inputs:
    if len(input) <= 0:
      return False
  
  return True



result1 = "True"
result2 = "asdvbfn"
result3 = "bsr"
if check_input([result1, result2, result3]) is True:
    print("1")
else:
    print("2") 
  
# {% if user.is_authenticated %}
# <div></div>
# {% else %}
#     <meta http-equiv="refresh" content="0; URL=../../Users/login" />
# {% endif %}