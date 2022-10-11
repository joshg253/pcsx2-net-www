import datetime
import glob
import json
import os
import re

id = input("ID Prefix (ie. 219): ")
## [2 New Plugins for Download](/143-2-new-plugins-for-download.html) {#new-plugins-for-download .contentheading}
title_and_alias_regex = "##\s?\[(.*)\]\((\/.*)\.html"
md_file = glob.glob(f'./article-backup/**/{id}*.md', recursive=True)[0]
title = ""
alias = ""
content = []
with open(md_file) as file:
  lines = file.readlines()
  found_title = False
  for line in lines:
    matches = re.findall(title_and_alias_regex, line)
    if len(matches) > 0:
      found_title = True
      title = matches[0][0]
      alias = matches[0][1]
      continue
    if found_title and ":::" not in line:
      content.append(line)

slug = title.replace(" ", "-").lower()
draft = "false"

date = None
json_file = glob.glob(f'./article-backup/**/{id}*.json', recursive=True)[0]
with open(json_file) as file:
  data = json.load(file)
  date = datetime.datetime.fromisoformat(data['date'])

summary = "TODO"

author_regex = "content=\"(.*)\".+author"
html_file = glob.glob(
    f'./article-backup/**/html-full/{id}*.html', recursive=True)[0]
author = ""
with open(html_file) as file:
  lines = file.readlines()
  for line in lines:
    matches = re.findall(author_regex, line)
    if len(matches) > 0:
      found_title = True
      author = matches[0]
      break

path = f"./content/blog/{date.year}/{slug}"
pathFile = f"{path}/index.md"
os.makedirs(path, exist_ok=True)
with open(pathFile, 'a') as f:
  f.write('---\n')
  f.write(f'title: \"{title.title().replace("Pcsx2", "PCSX2")}\"\n')
  f.write(f"date: {date.isoformat()}\n")
  f.write(f'summary: \"{summary}\"\n')
  f.write(f"draft: {draft}\n")
  f.write("tags:\n")
  f.write("  - TODO\n")
  f.write(f"mainAuthor: {author}\n")
  f.write("aliases:\n")
  f.write(f'  - \"{alias}\"\n')
  f.write(f'  - \"{alias}.html\"\n')
  f.write(f'  - \"{alias}.htm\"\n')
  f.write('---\n')
  f.writelines(content)

print(f"Wrote - {path}")
