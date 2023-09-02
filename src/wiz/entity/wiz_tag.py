
class WizTag(object):
    """ 为知笔记 TAG
    """
    # document 的 guid
    doc_guid: str = None

    # tag 的 guid
    guid: str = None

    name: str = None

    def __init__(self, doc_guid, guid, name) -> None:
        self.doc_guid = doc_guid
        self.guid = guid
        self.name = name
