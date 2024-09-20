urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"] 
dominios = [url[4:-4] for url in urls] #remove os 4 primeiros e os 4 ultimos digitos de cada url
print(dominios)