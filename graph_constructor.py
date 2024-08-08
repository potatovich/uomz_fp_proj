import wfdb
from other_methods import get_record, get_annotation, annotations_filter
from tkinter import messagebox


def show_graph(rec_name, req_sym, s_from, s_to): #Метод осуществляющий создание окна с графиком и выделенными в графе аннотациями
    try:
        record = get_record(rec_name, s_from, s_to)
        annotation_atr = get_annotation(rec_name, s_from, s_to)

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
        )
    except Exception:
        messagebox.showerror(title="Запуск приостановлен", message="Возникла ошибка на этапе отрисовки графика!")

# show_graph('databases/mit-bih-arrhythmia-database-1.0.0/100', ['[', ']', 'N'])