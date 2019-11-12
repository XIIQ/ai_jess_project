from os import getcwd
from os import listdir
from os.path import join
from os.path import isfile

class Template_Builder(object):
    """docstring for Template_Builder."""

    def __init__(self):
        super(Template_Builder, self).__init__()
        self.path = join(getcwd(),"Templates")
        self.templates = [
        {
        "name" : "age_groups",
        "slots" : [
        ["slot", "type", "STRING"]
        ]
        },
        {
        "name" : "authors",
        "slots" : [
        ["slot", "name", "STRING"]
        ]
        },
        {
        "name" : "books",
        "slots" : [
        ["slot", "score", "INTEGER"],
        ["slot", "name", "STRING"],
        ["multislot","genre","STRING"],
        ["slot","author","STRING"],
        ["slot","language","STRING"],
        ["slot","age_group","STRING"],
        ["slot","pacing","STRING"],
        ["slot","style","STRING"]
        ]
        },
        {
        "name" : "genres",
        "slots" : [
        ["slot", "type", "STRING"]
        ]
        },
        {
        "name" : "languages",
        "slots" : [
        ["slot", "type", "STRING"]
        ]
        },
        {
        "name" : "pacings",
        "slots" : [
        ["slot", "type", "STRING"]
        ]
        },
        {
        "name" : "styles",
        "slots" : [
        ["slot", "type", "STRING"]
        ]
        },
        {
        "name" : "users",
        "slots" : [
        ["slot", "username", "STRING"],
        ["multislot","genre","STRING"],
        ["slot","author","STRING"],
        ["slot","language","STRING"],
        ["slot","age_group","STRING"],
        ["slot","pacing","STRING"],
        ["slot","style","STRING"]
        ]
        }
        ]
        self.build_templates()

    def build_templates(self):
        for template in self.templates:
            output_file_data = "(deftemplate " + template["name"] + "\n"
            for slot in template["slots"]:
                if(slot[1] == "score"):
                    output_file_data += "\t(" + slot[0] + " " + slot[1] + " (default 0) (type " + slot[2] + "))\n"
                else:
                    output_file_data += "\t(" + slot[0] + " " + slot[1] + " (type " + slot[2] + "))\n"
            output_file_data += ")"

            with open(join(self.path,(template["name"] + "_template.clp")),"w+") as target:
                target.write(output_file_data)
                target.close()
