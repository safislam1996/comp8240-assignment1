import fandom

# setting the wiki series to JoJo's Bizarre Adventure
fandom.set_wiki("Jojo")
# I am choosing this character because the N=8 and he is my favorite character from the series!
josuke=fandom.page("Josuke Higashikata")
content=josuke.section("Showdown with Kira")

words = content.split()
content=' '.join(words) 

with open("fanwiki.txt", "w", encoding="utf-8") as file:
            file.write(content+"\n")