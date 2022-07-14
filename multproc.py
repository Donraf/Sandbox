# from multiprocessing import Process, Manager
# import os
#
#
# def f(arr, x):
#     arr.append(x)
#
#
# if __name__ == '__main__':
#     list_dir = os.listdir(r'C:\Users\Максим\Desktop\Texts_ALL')
#     manager = Manager()
#     vocab = manager.list()
#
#     while len(list_dir) > 0:
#         name_1 = list_dir[-1]
#         name_2 = list_dir[-2]
#         name_3 = list_dir[-3]
#         list_dir = list_dir[:-3]
#
#         p1 = Process(target=f, args=(vocab, name_1))
#         p2 = Process(target=f, args=(vocab, name_2))
#         p3 = Process(target=f, args=(vocab, name_3))
#         p1.start()
#         p2.start()
#         p3.start()
#         p1.join()
#         p2.join()
#         p3.join()
#
#         print(len(vocab))



# import os
#
# import fitz
#
# pdf_path = r'C:\Users\Максим\Desktop\ProcessedDocs'
# txt_path = r'C:\Users\Максим\Desktop\Texts_ALL'
#
# doc_list = os.listdir(pdf_path)
#
# with open(r'C:\Users\Максим\Desktop\Work\Word_stat\CSV\FILE_STAT.txt', 'w+', encoding='utf-8') as file_stat:
#     file_stat.write('NAME,NUM_PAGES,SIZE\n')
#
#     for file_num, doc_name in enumerate(doc_list):
#         print(f'File {file_num + 1}')
#
#         doc_pdf_path = os.path.join(pdf_path, doc_name)
#         doc_txt_path = os.path.join(pdf_path, doc_name)
#
#         page_counter = 0
#         pdf = fitz.open(doc_pdf_path)
#         for page in pdf:
#             page_counter += 1
#         pdf.close()
#
#         txt_size = os.path.getsize(doc_txt_path)
#
#         file_stat.write(f'{doc_name},{page_counter},{txt_size}\n')