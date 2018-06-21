##Алена Щевьева, БКЛ162
import os
import re

def get_str(): ##эта функция собирает словарь имя файла -- строка из первых букв всех строк
    l = os.listdir('poems')
    dict = {}
    for f in l: ##открываем все файлы в цикле
        if f.endswith('.TXT'):
            with open('poems' + os.sep + f, 'r', encoding='utf-8') as fin:
                text = fin.read().lower() ##читаем, приводим к нижнему регистру
                text = re.sub('[^a-z\n]', ' ', text) ##чистим мусор
                text = text.split('\n') ##разбиваем по строкам
            temp_str = '' ##временная строка
            for line in text: ##для каждой строки
                if line:
                    temp_str += line[0] ##добавляем первую букву во временную строку
            dict[f] = [temp_str]
    print(dict)
    return dict


def create_dict(): ##составляем словарь словоформ
    temp = []
    l = os.listdir('collectio4')
    for f in l: ##берем все слова из прозы
        with open('collectio4' + os.sep + f, 'r', encoding='utf-8') as fin:
            text = fin.read().lower()
        text = re.sub('[^a-z]', '', text)
        for word in text.split():
            temp.append(word)
    l = os.listdir('poems')
    for f in l: ##берем все слова из стихов
        if f.endswith('.TXT'):
            with open('poems' + os.sep + f, 'r', encoding='utf-8') as fin:
                text = fin.read().lower()
            text = re.sub('[^a-z]', ' ', text)
            for word in text.split():
                temp.append(word)
    temp = set(temp) ##удаляем повторяющиеся слова
    print(len(temp))
    return temp


def find_something(st, dict, n): ##ищем слова в наших строках
    for word in dict: ## для каждого слова в словаре
        for k in st: ##в каждой строке
            if len(word) >= n: ## ищем слова длиньше пяти букв
                try:
                    f = re.search(word, st[k][0])
                    if f:
                        st[k].append(f.group()) ## кладем слово в копилочку, если нашлось
                except:
                    continue
    return st


def post_work(dict, n): ##делаем красивый вывод
    with open('result_'+str(n)+'.csv', 'w', encoding='utf-8') as f: ##открываем csv-файл на нужную длину слов
        for k in dict:
            if k.endswith('txt'): ##пишем имя автора
                f.write(re.sub('_', ' ', k.split('.txt')[0]))
            else:
                f.write(re.sub('_', ' ', k.split('.TXT')[0]))
            if len(dict[k]) > 1:
                for word in dict[k][1:]:
                    f.write('\t' + word) ##пишем слова
            f.write('\n')
    with open('pure_stat_'+str(n)+'.csv', 'w', encoding='utf-8') as f: ##открываем csv-файл на нужную длину слов
        for k in dict:
            if k.endswith('txt'): ##пишем имя автора
                f.write(re.sub('_', ' ', k.split('.txt')[0]))
            else:
                f.write(re.sub('_', ' ', k.split('.TXT')[0]))
            f.write('\t' + str(len(dict[k][1:]))) ##пишем количество слов
            f.write('\n')


if __name__ == '__main__':
    strks = get_str()
    all_dic = create_dict()
    post_work(find_something(strks, all_dic, 5), 5)
    post_work(find_something(strks, all_dic, 4), 4)
    post_work(find_something(strks, all_dic, 3), 3)
    post_work(find_something(strks, all_dic, 2), 2)