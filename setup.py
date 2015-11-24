from distutils.core import setup
import py2exe
import numpy, scipy
import os

pref_files = []
app_files = []

for files in os.listdir('C:\\Python27\\Lib\\site-packages\\psychopy'
                        '\\preferences\\'):
    f1 = 'C:\\Python27\\Lib\\site-packages\\psychopy\\preferences\\' + files
    # print f1
    pref_files.append(f1)

for files in os.listdir('C:\\Python27\\Lib\\site-packages\\psychopy\\app\\'):
    f1 = 'C:\\Python27\\Lib\\site-packages\\psychopy\\app\\' + files
    # print f1
    app_files.append(f1)

all_files = [("psychopy\\preferences", pref_files)]

setup(console=['gui.py'],
      data_files=all_files,
      options={
          'py2exe': {
              'includes' : ['scipy.*', 'scipy.integrate', 'scipy.special.*',
                            'scipy.linalg.*', 'scipy.integrate',
                            'scipy.sparse.csgraph._validation',
                            'multiprocessing', 'PIL.*',
                            'psychopy.visual.*']
          }
      })