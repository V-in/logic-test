import json

data_set = json.loads(open('data/source_file_2.json', 'r').read())
managers = {}
watchers = {}

def process_one(item):
    for manager in item['managers']:
        project = {
            'name': item['name'],
            'priority': item['priority']
        }
        if manager not in managers:
            managers[manager] = [project]
        else:
            managers[manager].append(project)

    for watcher in item['watchers']:
        project ={
            'name': item['name'],
            'priority': item['priority']
        }
        if watcher not in watchers:
            watchers[watcher] = [project]
        else:
            watchers[watcher].append(project)

def run(data_set):
    # Transform
    for item in data_set:
        process_one(item)
    # Reorder
    for item in managers:
        managers[item].sort(reverse=True, key=lambda x: x['priority'])
        managers[item] = list(map(lambda x: x['name'], managers[item]))
    for item in watchers:
        watchers[item].sort(reverse=True, key=lambda x: x['priority'])
        watchers[item] = list(map(lambda x: x['name'], watchers[item]))

if __name__ == '__main__':
    run(data_set)
    with open('watchers.json', 'w') as f:
        f.write(json.dumps(watchers, indent=2))
    with open('managers.json', 'w') as f:
        f.write(json.dumps(managers, indent=2))
