# đây là thông tin từ database:
listDictionary =   [{"name":"trang chu","link":"/"},
                    {"name":"trang about-us","link":"/about-us"},
                    {"name":"trang san pham","link":"/product"},
                    ]


# for i in listDictionary:
#     print("name:",i['name'])
#     print("link",i['link'])

# # xử lý dữ liệu từ database về dạng object:

#1: tạo CLASS tên là Page:
class Page:
    def __init__(self,name,link):
        self.name = name
        self.link = link

#2: khởi tạo Object và đổ vào list:
listObject = []
for i in listDictionary:
    page = Page(i['name'],i['link'])
    listObject.append(page)

#print(listObject)
#print(listObject[0])
print(listObject[0].link)