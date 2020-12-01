from smashggpy.models.Event import Event
from smashggpy.util import Initializer
from smashggpy.util.QueryQueueDaemon import QueryQueueDaemon
import traceback

def get_api_key(auth_token_filename):
    API_KEY = None
    with open("auth_token.pass") as file:
        API_KEY = file.read().replace('\n', '')
    assert(API_KEY)
    return API_KEY

# TODO:
def get_slugs(url):
    """
    Input: smash.gg tournament URL, a string
    Output: two strings: a tournament_slug and an event_slug
    Suggestion: urllib.parse: https://docs.python.org/3/library/urllib.parse.html
    """
    return "stanford-melee-biweekly", "melee-singles"

def get_matches(url):
    list_of_matches = []

    API_KEY = get_api_key("auth_token.pass")

    Initializer.initialize(API_KEY, 'info')
    tournament_slug, event_slug = get_slugs(url)
    event = Event.get(tournament_slug, event_slug)
    sets = None
    try:
        sets = event.get_sets()
    except:
        traceback.print_exc()

    QueryQueueDaemon.kill_daemon()
    return list_of_matches

def main():
    get_matches("https://smash.gg/tournament/stanford-melee-biweekly/events/melee-singles/brackets/529945/900801")

if __name__ == "__main__":
    main()
