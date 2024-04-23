# 1번

eng_news = ("""This question is usually lost in the immediacy of the news cycle and 
            the demands of a business struggling to find a sustainable model, 
            but there are many newsrooms around the globe experimenting with new approaches 
            to audience engagement and thinking about impact.""")

word = input("Enter a word: ")
NEWS = eng_news.replace(word, word.upper())
print(NEWS)


# 2번

tomato_news = eng_news.replace(" ", "🍅")
# words = eng_news.split(" ")
# tomato_news = "🍅".join(words)
print(tomato_news)
