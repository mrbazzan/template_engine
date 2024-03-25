
import re

class TemplateSyntaxError(Exception):
    pass


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

        code = CodeBuilder()
        code.add_line("def render_function(context, do_dots):")
        code.indent()

        code.add_line("result = []")
        code.add_line("append_result = result.append")
        code.add_line("extend_result = result.extend")
        code.add_line("to_str = str")

        # buffer output strings
        buf = []
        def flush_buf_into_code():
            if len(buf) == 1:
                code.add_line("append_result(%s)" % buf[0])
            elif len(buf) > 1:
                code.add_line("extend_result([%s])" % ", ".join(buf))
            del buf[:]   # buf.clear()

        # parse control structure
        tokens = re.split(r"(?s)(\$\$.*?\$\$|\$\!.*?\!\$|\$\#.*?\#\$)", text)
        for token in tokens:
            if token.startswith("$#"):  # comment line
                continue

            elif token.startswith("$$"):  # variable expression
                var = token[2:-2].strip()
                buf.append("to_str(%s)" % var)

            elif token.startswith("$!"):  # tag
                flush_buf_into_code()

                words = token[2:-2].strip().split()
                if words[0] == "if":  # if tag
                    if len(words) != 2:
                        self._syntax_error(
                            "error in the use of 'if' tag",
                            words
                        )
                    code.add_line(
                        "if c_%s:" % (words[1])
                    )
                    code.indent()

                elif words[0] == "for":  # for tag
                    if len(words) != 4 or words[2] != "in":
                        self._syntax_error(
                            "error in the use of 'for' tag",
                            words
                        )
                    code.add_line(
                        "for c_%s in %s:" % (
                            words[1],
                            words[3]
                        )
                    )
                    code.indent()

                elif words[0].startswith("end"):  # end tag
                    code.dedent()

                else:
                    self._syntax_error("unknown tag", words[0])

            else:
                if token:  # ignore empty literal created by regex
                    buf.append(repr(token))

        flush_buf_into_code()

        code.add_line("return ''.join(result)")
        code.dedent()

    def _syntax_error(self, msg, cause):
        raise TemplateSyntaxError("%s: %r" % (msg, cause))
