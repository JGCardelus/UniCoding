import sys
import requests
from bs4 import BeautifulSoup as bs

def title(text):
    sys.stdout.write("\033[1;34m")
    print(text)
    sys.stdout.write("\033[0;0m")

class Web_Page:
    def __init__(self, url, depth_level):
        self.web_content = None
        self.url = url
        self.depth_level = depth_level

    def url_checks(self, url):
        get_url = True

        if url == "#":
            get_url = False
            return get_url

        # Do not get file that are not html
        url_blocks = url.split('.')
        url_extension = url_blocks[len(url_blocks) - 1]
        if url_extension in ["pdf", "css", "js", "jpg", "png", "jpeg"]:
            get_url = False
            return get_url

        return get_url


    def get(self):
        get_url = self.url_checks(self.url)

        if not get_url:
            self.web_content = None
            return self.web_content

        try:
            web_rqst = requests.get(self.url)
            self.web_content = web_rqst.text

            return self.web_content
        except:
            self.web_content = None
            return self.web_content

    def flush(self):
        self.web_content = None

class Email:
    def __init__(self, email, url):
        self.email = email
        self.found_in = [url]

class Email_Crawler:
    def __init__(self, url, max_depth_level=1):
        self.initial_web = Web_Page(url, 0)
        self.max_depth_level = max_depth_level

        self.web_pages = [self.initial_web]
        self.emails = []

    def start(self):
        while len(self.web_pages) > 0:
            web_page = self.web_pages[0]
            if web_page.depth_level <= self.max_depth_level:
                title("Scaning -- DL: %s // URL: %s" % (web_page.depth_level, web_page.url))
                self.scan(web_page)

            self.web_pages.pop(0)

    def scan(self, web_page):
        web_page.get()

        if web_page.web_content != None:
            scraper = bs(web_page.web_content, 'html.parser')
            a_tags = scraper.find_all('a', href=True)

            new_depth_level = web_page.depth_level + 1

            for a_tag in a_tags:
                link = a_tag['href']
                mail_position = link.find("mailto:")
                if mail_position > -1:
                    mail_position += len("mailto:")
                    self.add_email(link, web_page.url, mail_position)
                else:
                    new_web_page = Web_Page(link, new_depth_level)
                    self.web_pages.append(new_web_page)

        web_page.flush()
                
    def add_email(self, link, url, pos):
        link_list = list(link)
        email_list = link_list[pos:]
        email_link = "".join(email_list)

        exists = False
        print("     · Found: %s" % (email_link))
        for pos_email in self.emails:
            if pos_email.email == email_link:
                exists = True
                pos_email.found_in.append(url)
                print("         ## Exists, saving url")
                break

        if not exists:
            email = Email(email_link, url)
            self.emails.append(email)
            print("         ## Does not exist, saving")

    def show(self):
        print()
        print()
        print("******************************")
        print("           RESULTS")
        print("******************************")
        print()
        print()
        for email_obj in self.emails:
            title(email_obj.email)
            print("Found in: ")
            for url in email_obj.found_in:
                print("     · %s" % (url))


email_crawler = Email_Crawler("https://www.icai.comillas.edu/es/estudios/estudios-de-master/master")
email_crawler.start()
email_crawler.show()

