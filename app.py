from flask import Flask,render_template

app = Flask(__name__) # khởi tạo flask


listPage=["trang chủ","trang about-us","trang sản phẩm"]

listDictionary =   [{"name":"trang chủ","link":"/"},
                    {"name":"trang about-us","link":"/about-us"},
                    {"name":"trang sản phẩm","link":"/product"},
                    ]

# for i in listDictionary:
# print(i['name'])
# print(i['link'])

# xử lý dữ liệu từ database về dạng object:

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

        



# cấu hình đường dẫn ở trang chủ
@app.route('/')
def index():
    return render_template("home.html", pageObjects = listObject ,pages=listPage, person = "Thắng",title="Trang Web Đầu tiên")

@app.route('/about-us')
def about():
    return render_template("about.html")    

# bắt đầu chạy chương trình
if __name__ == "__main__":
    app.run()

