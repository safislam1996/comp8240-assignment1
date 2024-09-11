import wikipedia

actor= "Jon Stewart"
word_limit=500
page = wikipedia.search(actor)
page_content = wikipedia.page(page).content
words = page_content.split()
content=' '.join(words[:word_limit]) 

with open("wikipedia.txt", "w", encoding="utf-8") as file:
            file.write(content+"\n")