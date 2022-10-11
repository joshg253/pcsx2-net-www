# Just a quick script to help make a new hugo article
# and not miss any important configuration
from datetime import datetime
import os

tag = input("Main Tag (devblog/progress-report/none): ")
if tag not in ["devblog", "progress-report", "none"]:
  exit(1)
title = input("Article Title: ")
slug = title.replace(" ", "-").lower()
date = input("Date (YYYY-MM-DD): ")
date = datetime.fromisoformat(date)
draft = "false"
summary = input("Article Summary: ")
authors = input("Authors (comma sep. // or leave blank): ")
aliasLinks = input("Alias Links (comma sep.): ")
dateInput = input("Date (ISO timestamp, or leave blank): ")
if dateInput != "":
  date = dateInput

path = f"./content/blog/{date.year}/{slug}"
pathFile = f"{path}/index.md"
os.makedirs(path, exist_ok=True)
with open(pathFile, 'a') as f:
  f.write('---\n')
  f.write(f'title: \"{title.title().replace("Pcsx2", "PCSX2")}\"\n')
  f.write(f"date: {date}\n")
  f.write(f'summary: \"{summary}\"\n')
  f.write(f"draft: {draft}\n")
  if tag != "none":
    f.write("tags:\n")
    f.write(f'  - \"{tag}\"\n')
  if authors != "":
    f.write(f'mainAuthor: {authors.split(",")[0]}\n')
    if len(authors.split(",")) > 1 and authors.split(",")[0] != "":
      f.write("secondaryAuthors:\n")
      secondaryAuthors = authors.split(",")
      secondaryAuthors.pop()
      for author in secondaryAuthors:
        f.write(f'  - \"{author}\"\n')
  if len(aliasLinks.split(",")) > 0 and aliasLinks.split(",")[0] != "":
    f.write("aliases:\n")
    for alias in aliasLinks.split(","):
      f.write(f'  - \"{alias}\"\n')
      f.write(f'  - \"{alias}.html\"\n')
      f.write(f'  - \"{alias}.htm\"\n')
  f.write('---\n')
