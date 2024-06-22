import sys

def main():
    input = sys.stdin.read().strip().split('\n')
    index = 0
    num_entries = int(input[index].strip())
    index += 1
    books = []
    
    while index < len(input):
        if input[index].strip() == "* * * * * * * * * * *":
            break
        
        pages = int(input[index].strip())
        index += 1
        title = input[index].strip()
        index += 1
        author = input[index].strip()
        index += 1
        
        # Skip the line with "pages"
        index += 1
        
        # Store book details
        books.append((pages, title, author))
    
    # Sort books by pages, then by title
    books.sort(key=lambda book: (book[0], book[1]))
    
    # Output the sorted books
    for book in books:
        print(book[1])
        print(book[2])
        print(f"{book[0]} pages")
        print()

if __name__ == "__main__":
    main()
