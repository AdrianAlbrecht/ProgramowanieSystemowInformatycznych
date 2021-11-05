class FileManager:
    def __init__(self,file_name):
        self.file_name=file_name
    def read_file(text_dataa):
        f = open(text_dataa, 'r')
        file_contents = f.read()
        print(file_contents)
        f.close()
    def update_file(text_dataa):
        f = open(text_dataa, "a")
        f.write("Now the file has more content!")
        f.close()
