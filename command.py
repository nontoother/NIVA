import datetime
from pyjokes import pyjokes
from wikipedia import wikipedia


class Command:
    def __init__(self):
        pass

    def process_query(self, text_script):
        if "wikipedia" in text_script:
            return self.search_wikipedia(text_script)

        elif "joke" in text_script:
            return self.tell_joke()

        else:
            return None


    def search_whitelist(self, query):
        pass # todo: search from .csv file

    def search_trained_model(self, query):
        pass

    def search_wikipedia(self, query):
        query = query.replace("wikipedia", "")
        if query != "":
            try:
                wiki_prefix = "According to wikipedia, "
                return wiki_prefix + wikipedia.summary(query, sentences=3)
            except:
                print("some error in finding at wikipedia")

    def tell_joke(self):
        return pyjokes.get_joke()




