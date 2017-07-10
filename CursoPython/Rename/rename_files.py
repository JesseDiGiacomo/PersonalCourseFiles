import os

def rename_files():

    # 1 - Get file names from a folder
    file_list = os.listdir ("/Users/Js/Desktop/prank/")
    print (file_list)
    
    # 2 - for each file, rename filename
    for file_name in file_list:
        os.rename (file_name, fila_name.translate (none, "0123456789"))

    rename_files ()



