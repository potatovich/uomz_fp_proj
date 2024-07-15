import os
import codecs

def get_paths():
    paths = []

    for folders, _, files in os.walk('databases'):
        for fn in files:
            paths.append('\\'.join([folders, fn]))


    return [path[:-4] for path in list(filter(lambda p: 
                                            len(p.split('\\')) == 3 and 
                                            '.atr' in p.split('\\')[2] and not 
                                            '.atr-' in p.split('\\')[2], 
                                            paths))]

def get_sym_labels_and_descriptions():

    file = codecs.open('sym_label.txt', 'r', 'utf-8')
    labels = file.readlines()
    file.close()

    labels = [line.strip() for line in labels]

    file = codecs.open('sym_description_rus.txt', 'r', 'utf-8')
    descriptions = file.readlines()
    file.close()

    descriptions = [line.strip() for line in descriptions]
    
    labels_and_descriptions = [' '.join([l, d]) for l, d in zip(labels, descriptions)]

    return labels_and_descriptions