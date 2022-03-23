import os, re

with open(r"C:\Users\Максим\Desktop\PostgreSQL\script2.sql", "w+") as file:
    file.write("INSERT INTO test VALUES")
    # file_gen = os.walk(r"C:\Users\Максим\Desktop\PostgreSQL\PostgreSQL_Files")
    file_gen = os.walk(r"C:\Users\Максим\Desktop\sort\Meaningful")
    for file_path in file_gen:
        path_to_text_dir = file_path
        paths_to_file = [os.path.join(path_to_text_dir[0], filename) for filename in path_to_text_dir[2]]
    doc_quantity = len(paths_to_file)
    doc_counter = 0
    print(doc_quantity)
    for document in paths_to_file:
        # print(doc_counter)
        doc_counter += 1
        doc_id = re.search(r"(\d+)", document).group()
        file.write(f"\n('{doc_id}', false, '")
        with open(document, "r") as doc_file:
            for line in doc_file:
                file.write(line.replace("'", "''"))
        if doc_counter == doc_quantity:
            print("Hiya!")
            file.write("')")
        else:
            file.write("'),")
