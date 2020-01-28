The email crawler relays on three classes, Web_Page, Email and Email_Crawler. Email_Crawler is the main class, when it is initialized two parameters must be filled, the url of the page and the depth_level which is 1 by default.

```
email_crawler = Email_Crawler("https://www.icai.comillas.edu/es/estudios/estudios-de-master/master", 2)
```
After initializing the crawler, the start method must be called. This method will scan all the pages in <code>self.web_pages</code> which is an array that stores Web_Page objects. Before scanning the page, <code>web_page.get()</code> is called. This method checks the url, if it is a photo, css or js it does not get the page as it is not necessary, if it is not one of those it requests the page and saves the content. Once the page has been saved it scans the page for emails and urls. If a url is found, a <code>Web_Page</code> element is created which saves the url and has some special functions and it is saved in <code>sef.web_pages</code> to be scanned later. If an email (<code>self.add_email()</code> is the function called) is found it looks if it has been already saved, if it has, it saves the url in which the email has been saved, if it is the first time it appears it creates an <code>Email</code> object, which saves the url where it has been found and the email direction.
```
email_crawler.start()
email_crawler.show()
```
After scanning the pages it shows the emails and where they have been found.