import re
import os
from chardet.universaldetector import UniversalDetector
import codecs
from collections import defaultdict, OrderedDict

ENCODING = 'utf-8'
DICT_TOTAL_FILE = r'C:\Users\Максим\Desktop\Словари\danakt\russian_total_utf8.txt'
DICT_RUS_FILE = r'C:\Users\Максим\Desktop\Словари\danakt\russian_utf8.txt'
DICT_SURN_FILE = r'C:\Users\Максим\Desktop\Словари\danakt\russian_surnames_utf8.txt'


TEXT_DIR = r'C:\Users\Максим\Desktop\Texts_ALL'
SAN_DIR = r'C:\Users\Максим\Desktop\Texts_sanitized'
TEMP_ENC_DIR = r'C:\Users\Максим\Desktop\BINFF'

word_set = set()
with open(DICT_TOTAL_FILE, 'r', encoding=ENCODING) as file:
    for line in file:
        word_set.add(line.strip().lower())

true_words = defaultdict(int)
wrong_words = defaultdict(int)

list_dir = os.listdir(r'C:\Users\Максим\Desktop\Texts_sanitized')
for file_num, file_name in enumerate(list_dir):
    print(file_num + 1)
    with open(os.path.join(r'C:\Users\Максим\Desktop\Texts_sanitized', file_name), 'r', encoding=ENCODING) as file:
        for line in file:
            words_in_line = re.findall(r'\w+', line)
            for word in words_in_line:
                if word in word_set:
                    true_words[word] += 1
                else:
                    wrong_words[word] += 1


t_dict = OrderedDict(sorted(true_words.items()))
w_dict = OrderedDict(sorted(wrong_words.items()))

t_dict_q = OrderedDict(sorted(true_words.items(), key=lambda item: item[1]))
w_dict_q = OrderedDict(sorted(wrong_words.items(), key=lambda item: item[1]))

with open(r'C:\Users\Максим\Desktop\test_words\true_words.txt', 'w+', encoding=ENCODING) as file:
    for key in t_dict.keys():
        file.write(key + ': ' + str(t_dict[key]) + '\n')

with open(r'C:\Users\Максим\Desktop\test_words\wrong_words.txt', 'w+', encoding=ENCODING) as file:
    for key in w_dict.keys():
        file.write(key + ': ' + str(w_dict[key]) + '\n')

with open(r'C:\Users\Максим\Desktop\test_words\true_words_quantity.txt', 'w+', encoding=ENCODING) as file:
    for key in reversed(t_dict_q.keys()):
        file.write(key + ': ' + str(t_dict_q[key]) + '\n')

with open(r'C:\Users\Максим\Desktop\test_words\wrong_words_quantity.txt', 'w+', encoding=ENCODING) as file:
    for key in reversed(w_dict_q.keys()):
        file.write(key + ': ' + str(w_dict_q[key]) + '\n')

























# for file_path in [DICT_RUS_FILE, DICT_SURN_FILE]:
#     with open(file_path, 'r', encoding=ENCODING) as orig_file:
#         with open(DICT_TOTAL_FILE, 'a+', encoding=ENCODING) as new_file:
#             for line in orig_file:
#                 new_file.write(line)













# list_dir = os.listdir(TEXT_DIR)
# file_counter = 0
# for text in list_dir:
#     file_counter += 1
#     print(file_counter)
#
#     text_path = os.path.join(TEXT_DIR, text)
#     temp_enc_path = os.path.join(TEMP_ENC_DIR, text)
#     detector = UniversalDetector()
#     try:
#         with open(text_path, "rb") as file:
#             for line in file:
#                 detector.feed(line)
#                 if detector.done:
#                     break
#         detector.close()
#         det_result = detector.result["encoding"]
#         print(det_result)
#         if det_result != ENCODING:
#             wrong_encoding = det_result
#             with codecs.open(text_path, "rU", wrong_encoding) as wr_enc_file:
#                 with codecs.open(temp_enc_path, "w+", ENCODING) as cor_enc_file:
#                     for line in wr_enc_file:
#                         cor_enc_file.write(line)
#             text_path = temp_enc_path
#     except:
#         continue
#
#
#     new_text_path = os.path.join(SAN_DIR, text[:-4] + r'_sanitized.txt')
#     with open(text_path, "r", encoding=ENCODING) as orig_file:
#         with open(new_text_path, 'w+', encoding=ENCODING) as new_file:
#             for line in orig_file:
#                 new_file.write(re.sub(r"[^А-Яа-яA-Za-z\s]", ' ', line.lower()))

