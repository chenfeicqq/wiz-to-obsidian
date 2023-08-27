class WizImage(object):
    """ 在为知笔记文章中包含的本地图像

    在为知笔记中，本地图像不属于资源，也没有自己的 guid
    """
    # 原始图像的整个 HTML 内容，包括 <img src="index_files/name.jpg">
    outer_html: str = None

    # 仅包含图像的 src 部分
    src: str = None

    def __init__(self, outer_html: str, src: str) -> None:
        self.outer_html = outer_html
        self.src = src

    def is_http(self):
        return self.src.find("http") == 0
