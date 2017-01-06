

def get_src_id_from_file(filePath):
    f = open(filePath)

    srcIds = list()
    for line in f :
        start = line.index('srcOuterId:')
        end = line.index(' msg:')
        srcId = line[start+len('srcOuterId:'):end]
        srcIds.append(srcId)

    return srcIds

if __name__=="__main__":
    srcIds = get_src_id_from_file(r'E:\project\github\PythonProject\small_code\file.txt')
    print((',').join(srcIds))