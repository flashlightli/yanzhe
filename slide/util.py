from html.parser import HTMLParser
from lxml import html


def _get_rich_text(rich_text):
    """
    富文本标签转成标签
    :param rich_text:
    :return:
    """
    h = HTMLParser()
    rich_text = h.unescape(rich_text.encode("utf-8").decode("utf-8").replace("&amp;", "&").replace("\n", "<br>"))  # 富文本标签转成标签对象

    return rich_text


def gm_decode_html(rich_text):
    """
        匹配富文本信息
    :param safe_text: 包含html标签(实体标签)的文本信息
    :return: 仅展示 纯文本
    """
    if not rich_text:
        return ""

    rich_text = _get_rich_text(rich_text)
    element_obj = html.fromstring(rich_text)  # 转成 element 对象处理标签
    safe_text = html.tostring(element_obj, encoding="unicode", method="text")  # 仅获取文本
    return safe_text.replace(" ", "").replace("\n", "").replace("\t", "")