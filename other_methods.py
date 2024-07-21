import os
import codecs
import wfdb
import numpy


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

def get_syms_and_descriptions(symbols): #Метод, осуществляющий получение списка всех доступных для данного графика аннотаций

    file = codecs.open('sym_label.txt', 'r', 'utf-8')
    labels = file.readlines()
    file.close()

    labels = [line.strip() for line in labels]

    file = codecs.open('sym_description_rus.txt', 'r', 'utf-8')
    descriptions = file.readlines()
    file.close()

    descriptions = [line.strip() for line in descriptions]
    
    labels_and_descriptions = [' '.join([l, d]) for l, d in zip(labels, descriptions) if l in symbols]

    return labels_and_descriptions

def annotations_filter(anno_samp, anno_sym, req_sym): #Метод осуществляющий фильтрацию аннотаций 
    fil_sym = []
    fil_samp = []

    for samp, sym in zip(anno_samp, anno_sym):
        if sym in req_sym:
            fil_sym.append(sym)
            fil_samp.append(samp)

    return numpy.array(fil_samp[:]), fil_sym

def get_record(file_name, s_from, s_to): #Метод осуществляющий получение данных о графике

    record = wfdb.rdrecord( #Считывание данных (для построения графика) из .hea и .dat файлов
        record_name=file_name,
        sampfrom=s_from,
        sampto=s_to
    )

    return record

def get_annotation(file_name, s_from, s_to): #Метод осуществляющий получение данных об аннотации

    annotation_atr = wfdb.rdann( #Считывание данных (для построения аннотаций) из .atr файла(в некторых случаях вместо них идут .ari файлы, но в данном решении такие файлы игнорируются)
        record_name=file_name, 
        extension='atr',
        sampfrom=s_from,
        sampto=s_to
    )

    return annotation_atr

def get_sig_len(file_name): #Метод осуществляющий получение длины записи
    return wfdb.rdrecord(record_name=file_name).sig_len