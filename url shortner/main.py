import pyshorteners

def shortner(link):
    shortner = pyshorteners.Shortener()
    short_link = shortner.tinyurl.short(link)
    return short_link

url = input("Enter url:")
final = shortner(url)
print(f"Shortened url is :{final}")