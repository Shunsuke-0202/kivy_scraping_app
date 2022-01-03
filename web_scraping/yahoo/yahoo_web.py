import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.yahoo.co.jp/"


def yahoo_csv(url):
    #htmlの取得
    response = requests.get(url)

    with open("web_scraping/yahoo/yahoo.html", "w", encoding="UTF-8") as file:
        soup = BeautifulSoup(response.text, "html.parser")
        file.write(soup.prettify())  # きれいにしたHTMLを出力

        url_founds = soup.select(
            "li._2j0udhv5jERZtYzddeDwcv article.QLtbNZwO-lssuRUcWewbd a")  # url取得

        text_founds = soup.select(
            "li._2j0udhv5jERZtYzddeDwcv article.QLtbNZwO-lssuRUcWewbd a div._2cXD1uC4eaOih4-zkRgqjU")  # テキスト取得

        url_list = []
        text_list = []

        #urlをリストに追加
        for found in url_founds:
            url_list.append(found.get("href"))

        #for url in url_list:
        #    print(url)

        #テキストをリストに追加
        for found in text_founds:
            text_list.append(found.get_text())


        url_text_length = len(url_list)

        url_text_list=[list(e)for e in zip(text_list,url_list)]
            #print(url_text_list, "\n",i)

    #    print(url_text_list)

        with open("web_scraping/yahoo/yahoo_csv.csv", "w", encoding="utf_8_sig")as file:
            writer = csv.writer(file, lineterminator="\n")
            writer.writerows(url_text_list)


#        for i in range(len(url_list)):
#            url_text_list[i][0]=text_list[i]
#            text_list[i][0]=url_list[i]


if __name__ == "__main__":
    yahoo_csv()
