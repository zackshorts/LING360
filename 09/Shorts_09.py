import requests, random
from bs4 import BeautifulSoup as bs

# Write a Python program that web scrapes in order to create a small corpus of texts from the internet.
# Your program should start at a webpage that is hard-coded into your .py file. The program should randomly
# choose ten links on the starting webpage and then visit those other webpages. If there are fewer than ten,
# all the links available should be used. At each webpage, the program should web scrape the text and save it
# to a .txt file on your computer's hard drive. The program should perform any additional cleaning needed, for
# example, to exclude javascript function definitions. Each file should have a distinct name so that, when finished,
# the program will have written ten .txt files with the text of the ten websites your program visited.
# Turn into the CMS a .zip file with your Python program as a .py file, and ten .txt files with the text of
#  the webpages your web crawler visited.


# Scrapes stackoverflow and gets the links of questions on the landing page.
def generateLinks():
    links = []
    webpage = requests.get("https://stackoverflow.com/")
    soup = bs(webpage.text, 'html.parser')
    link_tags = soup.find_all("a", {"class": "question-hyperlink"})
    for link in link_tags:
        try:
            links.append(link.attrs['href'])
        except:
            print("Problem with URL. Moving on to next one.")

    sanitized_links = []
    for link in links:
        if link.startswith("https"):
            sanitized_links.append(link)
        else:
            sanitized_links.append("https://stackoverflow.com" + link)
    return sanitized_links


# This method will iterate through a list of links and scrape the content out of 10 of them. It excludes scripts.
def scrapeLinks(links):
    count = 0
    for link in links:
        if count == 10:
            break
        webpage = requests.get(link)
        soup = bs(webpage.text, 'html.parser')
        [s.extract() for s in soup(['script', 'noscript'])]
        all_text = soup.find_all("div", {"id": ["mainbar", "question-header"]})
        writeToTextFile(all_text, link, count)
        count += 1


# This method will take in text, a filename, and a filenumber and will create a .txt file in output folder.
def writeToTextFile(text, filename, filenumber):
    with open("output/" + str(filenumber) + ".txt", 'w') as text_file:
        text_file.write(filename + '\n\n')
        for line in text:
            text_file.write(line.get_text() + '\n')


# Create the list of all links.
# Shuffle the randomize the links
# Scrape the text from the links.
def run():
    links = generateLinks()
    random.shuffle(links)
    scrapeLinks(links)


run()
