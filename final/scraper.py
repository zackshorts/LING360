import urllib.request
from bs4 import BeautifulSoup


# Get rid of white space, lines, etc.
def sanitize(text):
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text


# eliminate all script and style elements
def extract_tags(soup):
    for script in soup(["script", "style"]):
        script.extract()  # rip it out


# This method will take in text, a filename, and a filenumber and will create a .txt file in output folder.
def writeToTextFile(text, filename):
    print("Writing to " + filename + ".txt")
    with open("output/" + filename + ".txt", 'w') as text_file:
        text_file.write(text)


url_2015 = "https://www.jpmorganchase.com/corporate/annual-report/2015/"
html_2015 = urllib.request.urlopen(url_2015).read()
soup_2015 = BeautifulSoup(html_2015, 'html.parser')
extract_tags(soup_2015)


url_2016 = "https://reports.jpmorganchase.com/investor-relations/2016/ar-ceo-letters.htm"
html_2016 = urllib.request.urlopen(url_2016).read()
soup_2016 = BeautifulSoup(html_2016, 'html.parser')
extract_tags(soup_2016)

url_2017 = "https://reports.jpmorganchase.com/investor-relations/2017/ar-ceo-letters.htm"
html_2017 = urllib.request.urlopen(url_2017).read()
soup_2017 = BeautifulSoup(html_2017, 'html.parser')
extract_tags(soup_2017)

url_2018 = "https://reports.jpmorganchase.com/investor-relations/2018/ar-ceo-letters.htm"
html_2018 = urllib.request.urlopen(url_2018).read()
soup_2018 = BeautifulSoup(html_2018, 'html.parser')
extract_tags(soup_2018)


# get text
text_2015 = soup_2015.get_text()
text_2015 = sanitize(text_2015)
text_2016 = soup_2016.get_text()
text_2016 = sanitize(text_2016)
text_2017 = soup_2017.get_text()
text_2017 = sanitize(text_2017)
text_2018 = soup_2018.get_text()
text_2018 = sanitize(text_2018)


def run():
    print("Starting program...\n\n")
    writeToTextFile(text_2015, '2015')
    writeToTextFile(text_2016, '2016')
    writeToTextFile(text_2017, '2017')
    writeToTextFile(text_2018, '2018')
    print("\n\nShutting down program...")


run()
