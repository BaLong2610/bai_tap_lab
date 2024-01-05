import xml.dom.minidom
path = r'G:\bai_tap\chuong_2\sample.XML'
doc = xml.dom.minidom.parse(path)
element = doc.getElementsByTagName('name')
print("%d element name :" % element.length)
for i in element:
    print(i.firstChild.nodeValue)
element2 = doc.getElementsByTagName('staff ')
print("%d element2 staff :" % element2.length)
for i in element2:
    print(i.firstChild.nodeValue)
element3 = doc.getElementsByTagName('salary')
print("%d element3 salary:" % element3.length)
for i in element3:
    print(i.firstChild.nodeValue)