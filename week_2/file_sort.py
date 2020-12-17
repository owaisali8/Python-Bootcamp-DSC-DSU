import os 

def sort_by_size_print(path):
    files_list = os.listdir(path)
    files_pair = []
    for file in files_list:
        location = os.path.join(path,file)
        size = os.path.getsize(location)
        files_pair.append([file,size])
    files_pair.sort(key=lambda s: s[1])
    files_pair.reverse()

    for i in range(len(files_pair)):
        print(f"{files_pair[i][0]:<25} <-- {files_pair[i][1]:<5} Bytes" )

path = input("Enter Path: ")
sort_by_size_print(path)