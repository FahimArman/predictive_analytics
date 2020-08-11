import urllib.request
myurl = "https://dailybrowsing.github.io/page/subtitle.html"
data = urllib.request.urlopen(myurl).read()
print(data)
