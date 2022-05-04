class News:
     def __init__(self,content,img,date,url):
        self.content = content
        self.img = img
        self.date = date
        self.url = url

class Source:
   def __init__(self,name,url):
       self.name =name
       self.url =url