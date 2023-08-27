class WizInternalLink(object):
    """ 嵌入 html 正文中的为知笔记内部链接，可能是笔记，也可能是附件
    """
    # 原始链接的整个 HTML 内容，包括 <a href="link....">名称</a>
    outer_html: str = None

    # 链接的 title
    title: str = None

    # 原始链接中的资源 guid，可能是 attachment 或者是 wiz_document.py
    guid: str = None

    # 值为 open_attachment 或者 open_document
    link_type: str = None

    def __init__(self, outer_html: str, guid: str, title: str, link_type: str) -> None:
        self.outer_html = outer_html
        self.guid = guid
        self.title = title
        self.link_type = link_type

    def is_open_attachment(self):
        return "open_attachment" == self.link_type

    def is_open_document(self):
        return "open_document" == self.link_type
