from pathlib import Path
import json
import frontmatter

static = Path('static') / Path('archive')

raw_archive = [x for x in static.rglob('*')]
project_dirs = [x for x in static.rglob('*') if x.is_dir()]

archive = []

for project in project_dirs:
    project_data = {}

    index = project / Path('index.md')
    with open(index, 'r') as f:
        d = frontmatter.load(f)
        project_data['title'] = d.metadata['title']
        project_data['date'] = d.metadata['date']
        project_data['tags'] = d.metadata['tags']
        project_data['text'] = d.content
        project_data['assets'] = []
    # Get assets
    for x in project.rglob('*'):
        if x.is_file() and x.name != 'index.md':
            project_data['assets'].append(
                f'/archive/{Path(x.parent.name) / x.name}'
            )
    archive.append(project_data)

print(archive)
with open('static/archive.json', 'w') as f:
    json.dump(
        {'archive' : archive},
        f,
        indent=4
    )
    
            


            



        