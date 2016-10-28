



from html.parser import HTMLParser;
 
import sys;
import urllib;
import urllib.request;

 
class MyParser(HTMLParser):
    def __init__ (self):
        HTMLParser.__init__(self);
        self.links = [];

    def handle_starttag (self,tag,attrs):
        
        if tag=='a':
            if len(attrs) == 0: 
                pass
            else:
                for (key,value) in attrs:
                    if key == 'href':
                        self.links.append(value);


        pass;
    def handle_endtag (self,tag):
        #print('</%s>'%tag);
        pass;

print ('===================html process===================')


start_url = "http://www.163.com";

wp = urllib.request.urlopen(start_url);
wp_content = wp.read();

#print(wp_content);
#fd = open('ProcessHtml/test.txt','r');
#content = fd.read();

YdnParser = MyParser();

YdnParser.feed(wp_content.decode('GBK'));


for hlink in YdnParser.links:
    print (hlink);

pass;

print(len(YdnParser.links));



