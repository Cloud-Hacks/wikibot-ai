import wikipedia

def search_wikipedia(query, limit):
    wikipedia.set_lang("en")
    search_results = wikipedia.search(query, results=limit)
    results = []
    for title in search_results:
        try:
            page = wikipedia.page(title)
            results.append({"url": page.url, "title": page.title, "text": page.summary})
        except wikipedia.PageError:
            continue
    return results