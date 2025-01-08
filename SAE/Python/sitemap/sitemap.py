with open("./sitemap/sitemap.txt", "r") as file:
    sitemap = file.read().strip().split("\n")

#def change_domain(sitemap, old_domain, new_domain):
#    return sitemap.replace(old_domain, new_domain)

def change_domain(sitemap, new_domain): # Aufgabe 1
    sitemap_changed = []
    for url in sitemap:
        parts = url.split("/")
        parts[0] = new_domain
        sitemap_changed.append("/".join(parts))
    return sitemap_changed

def change_structure(sitemap): # Aufgabe 5
    sitemap_changed = []
    for url in sitemap:
        if "news" in url:
            url = url.split("/")
            url.insert(url.index("main") + 1, url.pop(url.index("news")))
            sitemap_changed.append("/".join(url))
        else:
            sitemap_changed = (url)
    return sitemap_changed

sitemap_changed = change_domain(sitemap, "www.holzschule-calw.de")
sitemap_changed = change_structure(sitemap_changed)


with open("./sitemap/sitemap_changend", "w") as file:
    file.write("\n".join(sitemap_changed))