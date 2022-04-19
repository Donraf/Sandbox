import os
import re
import copy
import pytesseract
from pdf2image import convert_from_path, pdfinfo_from_path
from PIL import Image

from constants import *




## Запись в csv файл
IMG_PATH = r'C:\Users\Максим\Desktop\DS_Table_PT'
CSV_FILE = r'C:\Users\Максим\Desktop\table.csv'
img_dir = os.listdir(IMG_PATH)

key_dict = {
            "IsTable": 0,
            "NotTable": 1,
           }

with open(CSV_FILE, 'w') as csv_file:
    for image in img_dir:
        print(image)
        img_class = re.search(r'(?P<class>.+)_', image).group('class')
        print(img_class)
        csv_file.write(f'{image}, {key_dict[img_class]}\n')





# ## - Переименовка изображений
# TABLE_PATH = r'C:\Users\Максим\Desktop\Dataset_Tables\IsTable'
# NOT_TABLE_PATH = r'C:\Users\Максим\Desktop\Dataset_Tables\NotTable'
# IMG_PATH = r'C:\Users\Максим\Desktop\DS_Table_PT'
#
# pathes = [TABLE_PATH, NOT_TABLE_PATH]
#
# for path in pathes:
#     img_list = os.listdir(path)
#     class_name = re.search(r'\\(?P<class>\w+)$', path).group('class')
#     print(class_name)
#     mask = ['0' for x in range(len(str(len(img_list))))]
#     print(mask)
#     for idx, image in enumerate(img_list):
#         num = copy.copy(mask)
#         idx_len = len(str(idx))
#         num[-idx_len:] = str(idx)
#         img_index = ''.join(num)
#         try:
#             os.rename(os.path.join(path, image),
#                       os.path.join(path, rf'{class_name}_{img_index}.jpeg'))
#         except:
#             pass


# # --- Получение изображений
# file_counter = 0
# while len(os.listdir(PDF_FOLDER)) > 0:
#     for batch_ind in range(0, BATCH_SIZE):
#         if batch_ind >= len(os.listdir(PDF_FOLDER)):
#             break
#         file_counter += 1
#         file_name = os.listdir(PDF_FOLDER)[batch_ind]
#         print(file_name)
#         path_to_file = os.path.join(PDF_FOLDER, file_name)
#         page_number = pdfinfo_from_path(path_to_file, poppler_path=POPPLER_PATH)['Pages']
#         print(f'File {file_counter} has {page_number} pages.')
#
#     # --- PDF to Image - START
#         print(f"File {file_counter}: {file_name}. Converting from PDF to PPM")
#         image_dir_name = os.path.join(IMAGE_FOLDER, file_name[:-4])
#         if not os.path.exists(image_dir_name):
#             os.makedirs(image_dir_name)
#         convert_from_path(path_to_file, output_folder=image_dir_name,
#                           fmt="ppm", thread_count=4, poppler_path=POPPLER_PATH)
#         print(f"File {file_counter}: {file_name}. Converting from PPM to JPEG")
#         images = os.listdir(image_dir_name)
#         image_counter = 0
#         for image_name in images:
#             image_counter += 1
#             path_to_image = os.path.join(image_dir_name, image_name)
#             with Image.open(path_to_image) as image:
#                 image.save(path_to_image[:-4] + JPEG)
#             os.remove(path_to_image)
#         print(f"File {file_counter}. Created {image_counter} JPEG images.")
#         os.replace(os.path.join(PDF_FOLDER, file_name), os.path.join(USED_PDF_FOLDER, file_name))
#     # --- PDF to Image - END
