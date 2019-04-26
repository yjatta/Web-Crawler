import os

# every project a new directory


def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating Project ' + directory)
        os.makedirs(directory)


def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)

    if not os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(file_path, data):
    f = open(file_path, 'w')
    f.write(data)
    f.close()

#
# create_project_dir("CayorEnterprises")
# create_data_files('CayorEnterprises', 'https://CayorEnterprises.com')

# append data to an existing file


def append_data_to_file(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data + '\n')


# read a file and convert to a set for a faster performance

def file_to_set(file_path):
    results = set()
    with open(file_path, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# loop through a set and each item will be a line in file (set to file)


def set_to_file(file_path, links):
    delete_file_content(file_path)
    for link in sorted(links):
        append_data_to_file(file_path, link)


def delete_file_content(file_path):
    with open(file_path, 'w'):
        pass
