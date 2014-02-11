import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)


br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.open('http://gmail.com')
br.select_form(nr=0)

br.form['Email'] = 'user'
br.form['Passwd'] = 'password'
br.submit()

all_msg_links = [l for l in br.links(url_regex='\?v=c&th=')]
for msg_link in all_msg_links[0:3]:
    print msg_link
    
    br.follow_link(msg_link)
    html = br.response().read()
    soup = BeautifulSoup(html)
    msg = str(soup.findAll('div', attrs={'class': 'msg'})[0])

    print msg
 print html2text.html2text(msg)

    br.follow_link(text='Inbox')


br.follow_link(text='Sign out')
