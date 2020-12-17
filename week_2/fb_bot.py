from bs4 import BeautifulSoup
import requests
import csv

base_link = "https://www.facebook.com/"

def get_likes(list):
    global base_link
    likes = []
    for i in range(len(list)):
        response = requests.get(f'{base_link}{list[i][0]}')
        soup = BeautifulSoup(response.content, 'html.parser')
        likes.append(soup.select_one("span._52id._50f5._50f7").text)
    return likes

def extract_likes_in_list(list): #Remove Gibberish
    for i in range(len(list)):
        list[i] = list[i].replace('\u200f', '').replace("لائکس",'').replace(" ",'')
        
def main():
    page_names = []
    with open("likes.csv" , "r") as file:
        csv_reader = csv.reader(file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                page_names.append(row)

    likes = get_likes(page_names)
    extract_likes_in_list(likes)
    print(likes)

    with open("likes.csv",'w',encoding='utf-8',newline='') as file:
        csv_writer = csv.writer(file)
        line_count = 0
        for i in range(len(page_names)+1):
            if line_count == 0:
                csv_writer.writerow(["FB Page Link" ,"Likes"])
                line_count += 1
            else:   
                csv_writer.writerow([page_names[i-1][0], likes[i-1]])

if __name__ == "__main__":
    main()