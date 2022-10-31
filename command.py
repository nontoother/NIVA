import datetime
from pyjokes import pyjokes
from wikipedia import wikipedia


def search_wikipedia(query):
    query = query.replace("wikipedia", "")
    if query != "":
        try:
            wiki_prefix = "According to wikipedia, "
            return wiki_prefix + wikipedia.summary(query, sentences=3)
        except:
            print("some errors in finding at wikipedia")


def search_whitelist(query):
    pass  # todo: search from .csv file


def search_trained_model(query):
    pass


# todo:
def process_query(text_script):
    if "hello" in text_script:
        return "how can I help you"

    elif "wikipedia" in text_script:
        return search_wikipedia(text_script)

    elif "joke" in text_script:
        return pyjokes.get_joke()

    else:
        return None



