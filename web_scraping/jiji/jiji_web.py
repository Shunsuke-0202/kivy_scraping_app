import requests
import csv
from bs4 import BeautifulSoup


def jiji_csv(url):
    #htmlの取得
    response = requests.get(url)

    with open("web_scraping/jiji/jiji.html", "w", encoding="UTF-8") as file:
        soup = BeautifulSoup(response.text, "html.parser")
        file.write(soup.prettify())  # きれいにしたHTMLを出力

        url_founds = soup.select(
            "div.RankingContents dl.clearfix dd a")  # url取得

        text_founds = soup.select(
            "div.RankingContents dl.clearfix dd a")  # テキスト取得

        url_list = []
        text_list = []

        #urlをリストに追加
        for found in url_founds:
            i=found.get("href")
            url_list.append("https://www.jiji.com"+i)
            print("https://www.jiji.com"+i)

        #for url in url_list:
        #    print(url)

        #テキストをリストに追加
        for found in text_founds:
            text_list.append(found.get_text())
            print(found.get_text())


        url_text_length = len(url_list)

        url_text_list=[list(e)for e in zip(text_list,url_list)]
            #print(url_text_list, "\n",i)

    #    print(url_text_list)

        with open("web_scraping/jiji/jiji_csv.csv", "w", encoding="utf_8_sig")as file:
            writer = csv.writer(file, lineterminator="\n")
            writer.writerows(url_text_list)


#        for i in range(len(url_list)):
#            url_text_list[i][0]=text_list[i]
#            text_list[i][0]=url_list[i]


if __name__ == "__main__":
    jiji_csv()
