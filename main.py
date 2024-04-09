from database import create_anime, get_watchlist, update_anime_status, delete_anime
from utils import display_watchlist, get_user_input


def print_banner():
    banner = """

    


    
                 _             __          __   _       _     _      _     _   
     /\         (_)            \ \        / /  | |     | |   | |    (_)   | |  
    /  \   _ __  _ _ __ ___   __\ \  /\  / /_ _| |_ ___| |__ | |     _ ___| |_ 
   / /\ \ | '_ \| | '_ ` _ \ / _ \ \/  \/ / _` | __/ __| '_ \| |    | / __| __|
  / ____ \| | | | | | | | | |  __/\  /\  / (_| | || (__| | | | |____| \__ \ |_ 
 /_/    \_\_| |_|_|_| |_| |_|\___| \/  \/ \__,_|\__\___|_| |_|______|_|___/\__|
                                                                                                                                                                                                                        
By Sage!                                                                                                                                                                                                                                                                                                              
    """
    print(banner)
def main():
    print_banner()
    while True:
        
       
        print("\n=======================================\nAnime Watchlist:")
        display_watchlist()
        
        print("\nOptions:")
        print("1. Add Anime to Watchlist")
        print("2. Mark Anime as Watched")
        print("3. Mark Anime as Currently Watching")
        print("4. Remove Anime from Watchlist")
        print("5. Exit")
        
        choice = get_user_input("Enter your choice: ", int)

        if choice == 1:
            anime_name = input("Enter the name of the anime: ")
            create_anime(anime_name)
        elif choice == 2 or choice == 3:
            display_watchlist()
            anime_id = get_user_input("Enter the # of the anime from the WatchList: ", int)
            update_anime_status(anime_id, choice)
        elif choice == 4:
            display_watchlist()
            anime_id = get_user_input("the # of the anime from the WatchList: ", int)
            delete_anime(anime_id)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
