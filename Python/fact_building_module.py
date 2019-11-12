from os import getcwd
from os import listdir
from os.path import join
from os.path import isfile

class Fact_Builder(object):
    """docstring for Fact_Builder."""

    def __init__(self):
        super(Fact_Builder, self).__init__()
        self.path = join(getcwd(),"Facts")
        self.categories = [
        {
        "name" : "age_groups",
        "facts" : [
        {
        "type" : "young_adult"
        },
        {
        "type" : "children"
        },
        {
        "type" : "adult"
        }
        ]
        },
        {
        "name" : "books",
        "facts" : [
        {
        "name" : "book_1",
        "genre" : "thriller",
        "author" : "jk_rowling",
        "language" : "english",
        "age_group" : "young_adult",
        "pacing" : "slow",
        "style" : "conversational"
        },
        {
        "name" : "book_2",
        "genre" : "romance",
        "author" : "jk_rowling",
        "language" : "english",
        "age_group" : "young_adult",
        "pacing" : "medium",
        "style" : "spare"
        },
        {
        "name" : "book_3",
        "genre" : "detective",
        "author" : "sydney_sheldon",
        "language" : "english",
        "age_group" : "adult",
        "pacing" : "fast",
        "style" : "poetic"
        },
        {
        "name" : "book_4",
        "genre" : "science_fiction",
        "author" : "enid_blyton",
        "language" : "english",
        "age_group" : "children",
        "pacing" : "medium",
        "style" : "cspare"
        }
        ]
        },
        {
        "name" : "genres",
        "facts" : [
        {
        "type" : "dystopia"
        },
        {
        "type" : "detective"
        },
        {
        "type" : "educational"
        },
        {
        "type" : "fantasy"
        },
        {
        "type" : "mystery"
        },
        {
        "type" : "romance"
        },
        {
        "type" : "science_fiction"
        },
        {
        "type" : "thriller"
        }
        ]
        },
        {
        "name" : "languages",
        "facts" : [
        {
        "type" : "english"
        },
        {
        "type" : "hindi"
        }
        ]
        },
        {
        "name" : "pacings",
        "facts" : [
        {
        "type" : "slow"
        },
        {
        "type" : "medium"
        },
        {
        "type" : "fast"
        }
        ]
        },
        {
        "name" : "styles",
        "facts" : [
        {
        "type" : "conversational"
        },
        {
        "type" : "intricate"
        },
        {
        "type" : "poetic"
        },
        {
        "type" : "spare"
        }
        ]
        }
        ]
        self.build_facts()

    def build_facts(self):
        for category in self.categories:
            folder_path = join(self.path,category["name"])
            for fact in category["facts"]:
                filename = ""
                if("type" in fact):
                    filename = fact["type"]
                else :
                    filename = fact["name"]
                output_file_data = "(assert\n\t(" + category["name"] + "\n"
                for slot,value in fact.items():
                    output_file_data += "\t\t(" + slot + " \"" + value + "\")\n"
                output_file_data += "\t)\n)"

                with open(join(folder_path,(filename + "_fact.clp")),"w+") as target:
                    target.write(output_file_data)
                    target.close()
