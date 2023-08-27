class WizAttachment(object):
    """ 为知笔记附件

    在为知笔记中，附件属于一种资源，拥有自己的 guid
    """
    # 附件的 guid
    guid: str = None

    # 附件所属的文档 guid
    doc_guid: str = None

    # 附件的名称，一般是文件名
    name: str = None

    modified: str = None

    def __init__(self, guid: str, doc_guid: str, name: str, modified: str) -> None:
        self.guid = guid
        self.doc_guid = doc_guid
        self.name = name
        self.modified = modified
