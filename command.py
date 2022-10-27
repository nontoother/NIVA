import datetime
from pyjokes import pyjokes
from wikipedia import wikipedia


class Command:
    def __init__(self):
        pass

    def process_query(self, text_script):
        if "wikipedia" in text_script:
            self.search_whitelist(text_script)

        elif "joke" in text_script:
            self.tell_joke()

        else:
            pass


    def search_whitelist(self, query):
        pass # todo: search from .csv file

    def search_trained_model(self, query):
        pass

    def search_wikipedia(self, query):
        query = query.replace("wikipedia", "")
        wiki_prefix = "According to wikipedia, "
        return wiki_prefix + wikipedia.summary(query, sentences=3)

    def show_date(self):
        return datetime.datetime.now().strftime("%A %B %d, %Y")

    def show_time(self):
        return datetime.datetime.now().strftime("%I %M %p")

    def tell_joke(self):
        return pyjokes.get_joke()


