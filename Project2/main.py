# "Hooks" for dynamic binding

class Listener(object):
    """Abstract class defines required behavior"""
    def notify(self, msg: str):
        """All subclasses must implement 'notify'"""
        raise 