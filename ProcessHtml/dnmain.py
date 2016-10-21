



from html.parser import HTMLParser;
 
 
 
class MyParser(HTMLParser):
    def handle_starttag (self,tag,attrs):
        print('<%s>'%tag);
        pass;
    def handle_endtag (self,tag):
        print('</%s>'%tag);
        pass;

print ('===================html process===================')


YdnParser = MyParser();
fd = open('ProcessHtml/Ydn.html','r');
content = fd.read();
YdnParser.feed(content);


pass;

