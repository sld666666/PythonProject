
import  csv

class CsvWriter:

    def write(self, fileName, contents,  encoding='UTF-8'):

        with open(fileName, 'w', newline='') as f:
            fieldnames = ['title', 'score']
            writer = csv.DictWriter(f, fieldnames)
            for content in contents:
                for item in content:
                    try:
                        writer.writerow(item)
                    except Exception as e:
                        print("error in writerow:"+str(item)+":" + str(e))

