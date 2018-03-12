# _*_ coding:utf-8 _*_

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
# 获取PDF文件(文件名必须为英文)
fp = open('D:/gg/reinforcement_learning.pdf', 'rb')
# 创建一个与文档关联的解释器
parse = PDFParser(fp)
# PDF文档对象
doc = PDFDocument(parse)
# 连接解释器和文档对象
parse.set_document(doc)
# 创建PDF资源管理器
resource = PDFResourceManager()
# 参数分析器
laparam = LAParams()
# 创建一个聚合器
device = PDFPageAggregator(resource, laparams=laparam)
# 创建PDF页面解释器
interpreter = PDFPageInterpreter(resource, device)
# 使用文档对象得到页面集合
for page in PDFPage.create_pages(doc):
    # 使用页面解释器来读取
    interpreter.process_page(page)
    # 使用聚合器来获取内容
    layout = device.get_result()
    for out in layout:
        if hasattr(out, 'get_text'):
            print out.get_text()






