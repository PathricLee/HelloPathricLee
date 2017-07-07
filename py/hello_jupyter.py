
# coding: utf-8

# In[4]:

# %load subprocess_.py
#!/usr/bin/env python


"""
"""


import subprocess


cmd = ["mv", "tmp", "temp"]
call = subprocess.call
call(cmd)

cmd = ["ls", "-l"]
call(cmd)


# In[ ]:




# In[5]:

get_ipython().magic('run subprocess_.py')


# In[6]:

get_ipython().system('ls -l')


# In[7]:

get_ipython().system('pwd')


# In[8]:

import numpy as np
import pandas as pd
df = pd.DataFrame(np.arange(24).reshape(4, 6))


# In[9]:

df.T


# In[10]:

df


# ### learn to use jupyter
# 1. hello
# 2. world

# In[ ]:



