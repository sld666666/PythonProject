
def is_in(off_src_id, content):
    rtn = False

    for id in off_src_id:
        if content.find(id) > 0:
            rtn = True
            break

    return  rtn

if __name__=="__main__":

    f = open(r"E:\project\github\PythonProject\small_code\off_src_id.txt")
    off_src_id = list()
    for line in f :
        off_src_id.append(line.strip())

    print(off_src_id)

    error_file = open(r"E:\project\github\PythonProject\small_code\error.txt")
    for line in error_file:
        if not is_in(off_src_id, line):
            print(line)
