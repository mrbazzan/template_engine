
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
