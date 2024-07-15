import wfdb
import numpy

def annotations_filter(anno_samp, anno_sym, req_sym): #Метод осуществляющий фильтрацию аннотаций 
    fil_sym = []
    fil_samp = []

    for samp, sym in zip(anno_samp, anno_sym):
        if sym in req_sym:
            fil_sym.append(sym)
            fil_samp.append(samp)

    return numpy.array(fil_samp[:]), fil_sym

def get_record_and_annotation(rec_name): #Метод осуществляющий получение данных о графике и аннотации
    record = wfdb.rdrecord( #Считывание данных (для построения графика) из .hea и .dat файлов
        record_name=rec_name,
    )

    annotation_atr = wfdb.rdann( #Считывание данных (для построения аннотаций) из .atr файла(в некторых случаях вместо них идут .ari файлы, но в данном решении такие файлы игнорируются)
        record_name=rec_name, 
        extension='atr',
    )

    return record, annotation_atr

def show_graph(rec_name, req_sym): #Метод осуществляющий за создание окна с графиком и аннотациями

    record, annotation_atr = get_record_and_annotation(
        rec_name=rec_name
    )

    fil_samples, fil_symbols = annotations_filter( #Вызов метода фильтрации аннотаций
        anno_samp=annotation_atr.sample, 
        anno_sym=annotation_atr.symbol,
        req_sym=req_sym
    )

    wfdb.plot_items( #Построение графика + фильт. аннотаций
        signal=record.p_signal, 
        ann_samp=[fil_samples for _ in range(len(record.sig_name))],
        ann_sym=[fil_symbols for _ in range(len(record.sig_name))],
        title=rec_name,
        figsize=(15, 7),
        sharex=True,
        sharey=True,
        # time_units='seconds'
    )

# show_graph('databases/mit-bih-arrhythmia-database-1.0.0/100', ['[', ']', 'N'])