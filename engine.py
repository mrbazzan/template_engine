
class CodeBuilder:

    INDENT_STEPS = 4

    def __init__(self):
        self.code = []
        self.indent_level = 0

    def add_line(self, line):
        self.code.extend([' '*self.indent_level, line, '\n'])

    def indent(self):
        self.indent_level += self.INDENT_STEPS

    def dedent(self):
        self.indent_level -= self.INDENT_STEPS

    def __str__(self):
        return "".join(self.code)


class Template:
    def __init__(self, text, *contexts):
        """
        Template constructor

        :contexts: dictionaries of values. Good for
                   custom filters.
        """
        self.content = {}
        for context in contexts:
            self.content.update(context)
