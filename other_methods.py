import os
import codecs
import wfdb
import numpy
from tkinter import messagebox


def get_paths(): #Метод, осуществляющий получение путей до всех файлов в подпапках папки databases
    try:
        paths = []
        f_paths = []
        
        for folders, _, files in os.walk('databases'):
            for fn in files:
                paths.append('\\'.join([folders, fn]))

        for path in paths:
            if '.atr' in path[len(path) - 4:] and not '.atr-' in path[len(path) - 4:]:
                f_paths.append(path[:-4])
        
        return f_paths
    except Exception:
        messagebox.showerror(title="Запуск приостановлен", message="Возникла ошибка на этапе получения путей до всех файлов в подпапках папки databases!")

def get_syms_and_descriptions(symbols): #Метод, осуществляющий получение списка всех доступных для данного графика аннотаций
    try:
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
    except Exception:
        messagebox.showerror(title="Запуск приостановлен", message="Возникла ошибка на этапе получения доступных для данного сигнала аннотаций!")

def annotations_filter(anno_samp, anno_sym, req_sym): #Метод осуществляющий фильтрацию аннотаций 
    try:
        fil_sym = []
        fil_samp = []

        for samp, sym in zip(anno_samp, anno_sym):
            if sym in req_sym:
                fil_sym.append(sym)
                fil_samp.append(samp)

        return numpy.array(fil_samp[:]), fil_sym
    except Exception:
        messagebox.showerror(title="Запуск приостановлен", message="Возникла ошибка на этапе фильтрации аннотаций!")

def get_record(file_name, s_from, s_to): #Метод осуществляющий получение данных о графике
    try:
        record = wfdb.rdrecord( #Считывание данных (для построения графика) из .hea и .dat файлов
            record_name=file_name,
            sampfrom=s_from,
            sampto=s_to
        )

        return record
    except Exception:
            messagebox.showerror(title="Запуск приостановлен", message="Возникла ошибка на этапе получения данных о сигнале!")

def get_annotation(file_name, s_from, s_to): #Метод осуществляющий получение данных об аннотации
    try:
        annotation_atr = wfdb.rdann( #Считывание данных (для построения аннотаций) из .atr файла(в некторых случаях вместо них идут .ari файлы, но в данном решении такие файлы игнорируются)
            record_name=file_name, 
            extension='atr',
            sampfrom=s_from,
            sampto=s_to,
            shift_samps=True
        )

        return annotation_atr
    except Exception:
        messagebox.showerror(title="Запуск приостановлен", message="Возникла ошибка на этапе получения данных об аннотации!")

def get_sig_len(file_name): #Метод осуществляющий получение длины записи
    try:
        return wfdb.rdrecord(record_name=file_name).sig_len
    except Exception:
        messagebox.showerror(title="Запуск приостановлен", message="Возникла ошибка на этапе получения длины записи!")
        