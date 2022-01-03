from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.text import LabelBase,DEFAULT_FONT
from kivy.resources import resource_add_path


from web_scraping.yahoo import yahoo_web
from web_scraping.jiji import jiji_web

import webbrowser
import csv
from functools import partial

resource_add_path("font")
LabelBase.register(DEFAULT_FONT,"NotoSansJP-Black.otf")


class MainScreen(BoxLayout):

    def update(self,arg):
        print("success")
        with open(self.yahoo_filename,"r",encoding="utf-8") as f:
            reader=csv.reader(f)
            header=next(reader)
            line=[row for row in reader]
            for i in range(len(line)):
                self.yahoo_title_list.append(line[i][0])
                self.yahoo_url_list.append(line[i][1])

        with open(self.jiji_filename,"r",encoding="utf-8") as f:
            reader=csv.reader(f)
            header=next(reader)
            line=[row for row in reader]
            for i in range(len(line)):
                self.jiji_title_list.append(line[i][0])
                self.jiji_url_list.append(line[i][1])

    def yahoo_openpage(self,instance,arg):
        webbrowser.open(self.yahoo_url_list[instance]) #ページを開く関数

    def jiji_openpage(self,instance,arg):
        webbrowser.open(self.jiji_url_list[instance])



    def yahoo_callback(self,arg):
        yahoo_web.yahoo_csv("https://www.yahoo.co.jp/")

    def jiji_callback(self,arg):
        jiji_web.jiji_csv("https://www.jiji.com/")

    def __init__(self,**kwargs):
        super(MainScreen,self).__init__(**kwargs)

        self.yahoo_filename="web_scraping/yahoo/yahoo_csv.csv"
        self.jiji_filename="web_scraping/jiji/jiji_csv.csv"

        self.yahoo_title_list=[]
        self.yahoo_url_list=[]

        self.jiji_title_list=[]
        self.jiji_url_list=[]

        self.i=0

        self.yahoo_callback(self)
        self.jiji_callback(self)

        self.update(self)

        layout_wrapper=BoxLayout(orientation="vertical")
        content_wrapper=BoxLayout(orientation="vertical",size_hint_y=3)
        content2_wrapper=BoxLayout(orientation="vertical",size_hint_y=3)
        scroll_container=BoxLayout(size_hint_y=0.8)

        scroll_wrapper=ScrollView(size_hint_y=1)
        scroll2_wrapper=ScrollView(size_hint_y=1)
        btn_wrapper=BoxLayout(size_hint_y=0.2)

        yahoo_btn_list=[]
        yahoo_btn_url_list=[]

        jiji_btn_list=[]
        jiji_btn_url_list=[]

        searchbtn_list=[]

        for i in range(len(self.yahoo_title_list)):
            yahoo_btn_list.append(Button(text=f"{self.yahoo_title_list[i]}"))
            content_wrapper.add_widget(yahoo_btn_list[i])
            yahoo_btn_list[i].bind(on_press=partial(self.yahoo_openpage,i))

        for i in range(len(self.jiji_title_list)):
            jiji_btn_list.append(Button(text=f"{self.jiji_title_list[i]}"))
            content2_wrapper.add_widget(jiji_btn_list[i])
            jiji_btn_list[i].bind(on_press=partial(self.jiji_openpage,i))


        for self.i in range(1):
            searchbtn_list.append(Button(text="更新"))
            searchbtn_list[self.i].bind(on_press=self.update)
            btn_wrapper.add_widget(searchbtn_list[self.i])


        scroll_wrapper.add_widget(content_wrapper)
        scroll2_wrapper.add_widget(content2_wrapper)
        scroll_container.add_widget(scroll_wrapper)
        scroll_container.add_widget(scroll2_wrapper)
        #layout_wrapper.add_widget(scroll_wrapper)
        layout_wrapper.add_widget(scroll_container)
        layout_wrapper.add_widget(btn_wrapper)
        self.add_widget(layout_wrapper)    #layout_wrapper -> scroll_wrapper -> content_wrapper
                                           #               -> btn_wrapper



class ScrapingApp(App):
    def build(self):
        self.title="テスト"
        return MainScreen()


if __name__=="__main__":
    ScrapingApp().run()










"""
filename="csvfile.csv"
with open(filename,"r") as f:
    reader=csv.reader(f)
    header=next(reader)
    line=[row for row in reader]
    print(line[0])
    print(line)
"""
