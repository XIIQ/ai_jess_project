from os import getcwd
from os import listdir
from os.path import join
from os.path import isfile

class Setup(object):
    """docstring for Setup."""

    def __init__(self):
        super(Setup, self).__init__()
        self.path = getcwd()
        self.build_register_templates_clp()
        self.build_init_clp()
        self.path = join(self.path,"init.clp")
        if("\\" in self.path):
            self.path = self.path.replace("\\","\\\\")
        print("(batch \"" + self.path +"\")")

    def build_init_clp(self):
        dir_list = listdir(self.path)
        file_data = "(reset)\n"

        for file_name in dir_list:
            full_path = join(self.path,file_name)
            if(isfile(full_path) and ".clp" in file_name and (not "init.clp" == file_name)):
                if("\\" in full_path):
                    full_path = full_path.replace("\\","\\\\")
                file_data += "(batch \"" + full_path +"\")\n"

        file_data += "(printout t \"The application is initialized and ready to use!!\" crlf)\n"

        with open(join(self.path,"init.clp"),"w+") as target:
            target.write(file_data)
            target.close()

    def build_register_templates_clp(self):
        dir_list = listdir(join(self.path,"Templates"))
        file_data = ""

        for file_name in dir_list:
            full_path = join(self.path,"Templates",file_name)
            if(isfile(full_path) and ".clp" in file_name):
                if("\\" in full_path):
                    full_path = full_path.replace("\\","\\\\")
                file_data += "(batch \"" + full_path +"\")\n"

        file_data += "(printout t \"All the templates are registered and ready to use!!\" crlf)\n"

        with open(join(self.path,"register_templates.clp"),"w+") as target:
            target.write(file_data)
            target.close()


if __name__ == "__main__":
    Setup()
