"""
    ANSYS mechanical script parser
"""

INPUT_FILE_LOCATION = "./script.py"

# inputs
VALUE1 = 100
VALUE2 = 200
VALUE3 = 300
# context: key value pairs need to be replaced
context = {"input1": VALUE1, "input2": VALUE2}


class Parser(object):
    """
        script parser class
    """

    def __init__(self, file, context):
        """
        :param file <string> : script file location
        :param context <dict> : key value pair to be replaced
        :return <dict> : rendered data
        """
        self.file = file
        self.context = context

    def stringify(self, file):
        """read given file and and return as srting
        :param file <string> : input file location 
                example : 
                    1) ./file.txt for mac or linux
                    2) .\file.rxt for windows
        return : string

        """
        with open(file, "r") as file:
            data = file.read()
        return str(data)

    def render_context(self, sentance, context):
        """replace given text with provided context
        :param sentance: <string> input text stream
        :param context: <dict> key value pairs to be replaced
        :return <string> : rendered string
        """
        for key, value in context.items():
            sentance = sentance.replace(str(key), str(value))
        return sentance

    def render(self):
        """
            returns test with replaced key value pairs
        """

        sentance = self.stringify(self.file)
        data = self.render_context(sentance, self.context)
        return data


utils = Parser(INPUT_FILE_LOCATION, context)
at_cmd = utils.render()
print(at_cmd)
