import os 

class Folder():

    def __init__(self):
        self.path = ""
        self .content = []

    def set_path(self, path):
        self.path = path
        if self.path[len(path) - 1] != "/":
            self.path += "/"

    def obtain_content(self):
        result = False
        if len(self.path) == 0:
            print("no path for the folder")
        else:
            try:
                self.content = os.listdir(self.path)
                result = True
            except Exception as e:
                print("Error: reading directory :", e)
        return result

    def is_existing_in(self, fold, my_name):
        res = False
        for entry in fold.content:
            if entry == my_name:
                res = True
        return res

    def create(self):
        res = False

        if len(self.path) == 0:
            print("Error: need a path to create dir")
        else:
            try:
                os.mkdir(self.path)
                res = True
            except Exception as e:
                print("Error : creating the folder : ", e)
                quit(84)
        return res

    def pop_dir_in_content(self):
        new_content = []

        for idx, elt in enumerate(self.content):
            path = self.path + elt
            if not os.path.isdir(path):
                new_content.append(self.content[idx])
        self.content = new_content

    def get_extension(self, filename):
        length = len(filename) - 1
        extension = ""

        while ((filename[length] != ".") and (length > 0)):
            length -= 1
        if length != 0:
            while length < len(filename):
                extension += filename[length]
                length += 1
        return extension

    def get_entry_path(self, entry):
        return self.path + entry

    def mv_file(self, entry, target):
        try:
            os.rename(self.get_entry_path(entry), target.get_entry_path(entry))
        except Exception as e:
            print("Error : move the file :", e)


        