
import os
import glob

id = input("ID Prefix (ie. 219): ")
for f in glob.glob(f'./article-backup/**/{id}*', recursive=True):
  os.remove(f)
