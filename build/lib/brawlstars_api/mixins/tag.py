class TagMixin:
    @staticmethod
    def clean_tag(tag):
        """clean up tag."""
        if tag is None:
            return None
        t = tag
        if isinstance(t, list):
            t = t[0]
        if isinstance(t, tuple):
            t = t[0]
        if t.startswith('#'):
            t = t[1:]
        t = t.strip()
        t = t.upper()
        t = t.replace('O', '0')
        t = t.replace('B', '8')
        return t
