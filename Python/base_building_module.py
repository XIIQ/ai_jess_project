from os import getcwd
from os import listdir
from os.path import join
from os.path import isfile

class Base_Builder(object):
    """docstring for Base_Builder."""

    def __init__(self):
        super(Base_Builder, self).__init__()
        self.path = getcwd()
        self.init_build()
        self.return_batch_code()

    def init_build(self):
        self.build_register_templates_clp()
        self.build_register_facts_clp()
        self.build_register_queries_clp()
        self.build_register_functions_clp()
        self.build_init_clp()

    def build_register_templates_clp(self):
        folder_path = join(self.path,"Templates")
        folder_contents = listdir(folder_path)

        output_file_data = ""
        for file_name in folder_contents:
            absolute_file_path = join(folder_path,file_name)
            if(isfile(absolute_file_path) and ".clp" in absolute_file_path):
                output_file_data += "(batch \"" + self.return_os_compatible_url(absolute_file_path) +"\")\n"
        output_file_data += "(printout t \"All the templates are registered and ready to use!!\" crlf)\n"

        with open(join(self.path,"1_register_templates.clp"),"w+") as target:
            target.write(output_file_data)
            target.close()

    def build_register_facts_clp(self):
        folder_path = join(self.path,"Facts")
        folder_contents = listdir(folder_path)

        output_file_data = ""
        for sub_folder in folder_contents:
            sub_folder_path = join(folder_path,sub_folder)
            sub_folder_contents = listdir(sub_folder_path)

            for file_name in sub_folder_contents:
                absolute_file_path = join(sub_folder_path,file_name)
                if(isfile(absolute_file_path) and ".clp" in absolute_file_path):
                    output_file_data += "(batch \"" + self.return_os_compatible_url(absolute_file_path) +"\")\n"
        output_file_data += "(printout t \"All the facts are registered and ready to use!!\" crlf)\n"

        with open(join(self.path,"2_register_facts.clp"),"w+") as target:
            target.write(output_file_data)
            target.close()

    def build_register_queries_clp(self):
        folder_path = join(self.path,"Queries")
        folder_contents = listdir(folder_path)

        output_file_data = ""
        for file_name in folder_contents:
            absolute_file_path = join(folder_path,file_name)
            if(isfile(absolute_file_path) and ".clp" in absolute_file_path):
                output_file_data += "(batch \"" + self.return_os_compatible_url(absolute_file_path) +"\")\n"
        output_file_data += "(printout t \"All the queries are registered and ready to fire!!\" crlf)\n"

        with open(join(self.path,"3_register_queries.clp"),"w+") as target:
            target.write(output_file_data)
            target.close()

    def build_register_functions_clp(self):
        folder_path = join(self.path,"Functions")
        folder_contents = listdir(folder_path)

        output_file_data = ""
        for sub_folder in folder_contents:
            sub_folder_path = join(folder_path,sub_folder)
            sub_folder_contents = listdir(sub_folder_path)

            for file_name in sub_folder_contents:
                absolute_file_path = join(sub_folder_path,file_name)
                if(isfile(absolute_file_path) and ".clp" in absolute_file_path):
                    output_file_data += "(batch \"" + self.return_os_compatible_url(absolute_file_path) +"\")\n"
        output_file_data += "(printout t \"All the functions are registered and ready to use!!\" crlf)\n"

        with open(join(self.path,"4_register_functions.clp"),"w+") as target:
            target.write(output_file_data)
            target.close()

    def build_init_clp(self):
        folder_path = self.path
        folder_contents = listdir(folder_path)

        output_file_data = "(clear)\n(reset)\n"
        for file_name in folder_contents:
            absolute_file_path = join(folder_path,file_name)
            if(isfile(absolute_file_path) and ".clp" in absolute_file_path and (not file_name == "init.clp")):
                output_file_data += "(batch \"" + self.return_os_compatible_url(absolute_file_path) +"\")\n"
        output_file_data += "(printout t \"The application is initialized and ready to use!!\" crlf)\n"

        with open(join(self.path,"init.clp"),"w+") as target:
            target.write(output_file_data)
            target.close()

    def return_os_compatible_url(self,url):
        if("\\" in url):
            url = url.replace("\\","\\\\")
        return url

    def return_batch_code(self):
        command = "(batch \"" + self.return_os_compatible_url(join(self.path,"init.clp")) + "\")"
        print(command)
