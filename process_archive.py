from pathlib import Path
import json

static = Path('static') / Path('archive')

raw_archive = [x for x in static.rglob('*')]
project_dirs = [x for x in static.rglob('*') if x.is_dir()]

archive = {}

def parse_md(txt:str):
    md = {}
    for line in txt:
        if line.startswith('title:'):
            md['title'] = line.split(':', 1)[1].lstrip().rstrip()
        elif line.startswith('date:'):
            md['date'] = line.split(':', 1)[1].lstrip().rstrip()

    blurb = [x for x in txt if not x.startswith('title:') and not x.startswith('date:')]
    md['text'] = blurb
    return md

archive = []

for project in project_dirs:
    project_data = {}

    index = project / Path('index.md')
    with open(index, 'r') as f:
        project_data = parse_md(f.readlines())
        project_data['assets'] = []
    # Get assets
    for x in project.rglob('*'):
        if x.is_file() and x.name != 'index.md':
            project_data['assets'].append(
                f'/archive/{Path(x.parent.name) / x.name}'
            )
    archive.append(project_data)

with open('static/archive.json', 'w') as f:
    json.dump(
        {'archive' : archive},
        f,
        indent=4
    )
    
            


            



        