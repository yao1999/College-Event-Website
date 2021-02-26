
# this is for me to test if the python code is right or not
# I'll delete this when we submit this

from datetime import datetime

# now = datetime.now()

current_time = datetime.now().strftime("%H:%M:%S")
print("Current Time =", current_time)
  
# {% if user.is_authenticated %}
# <div></div>
# {% else %}
#     <meta http-equiv="refresh" content="0; URL=../../Users/login" />
# {% endif %}