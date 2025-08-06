def get_search_keyword():
    while True:
        keyword = input("Enter a search keyword: ").strip()
        if keyword:
            return keyword
        else:
            print("Keyword cannot be empty. Please try again.")

if __name__ == "__main__":
    keyword = get_search_keyword()
    print(f"Search keyword set to: {keyword}")
