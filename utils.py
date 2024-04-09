from database import get_watchlist

def display_watchlist():
    watchlist = get_watchlist()
    if watchlist:
        for anime in watchlist:
            print(f"{anime[0]}. {anime[1]} - {'Watched' if anime[2] == 2 else 'Currently Watching' if anime[2] == 1 else 'To Watch'}")
    else:
        print("Watchlist is empty.")

def get_user_input(prompt, data_type):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")
