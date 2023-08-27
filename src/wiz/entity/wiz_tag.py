
class WizTag(object):
    """ 为知笔记 TAG
    """
    # tag 的 guid
    guid: str = None

    name: str = None

    modified: str = None

    def __init__(self, guid, name, modified) -> None:
        self.guid = guid
        self.name = name
        self.modified = modified
