def task2(records):
    borrowed_books = {}
    for record in records:
        try:
            title,days=record.split(" - ")
            days=int(days)
            if title in borrowed_books:
                borrowed_books[title] += days
            else:
                borrowed_books[title] = days
        except ValueError:
            print(f"Invalid record format: '{record}'. Skipping.")
        # Set #
        unique_titles=set(borrowed_books.keys())
        # Maximum , Minimum #
        most_borrowed = max(borrowed_books.items(), key=lambda x: x[1])
        least_borrowed = min(borrowed_books.items(), key=lambda x: x[1])
        # Average #
        total_borrowed=sum(borrowed_books.values())
        average_days=total_borrowed/len(borrowed_books)
        # Sort #
        sorted_books = sorted(borrowed_books.items(), key=lambda x: x[1], reverse=True)

        print("Library Borrowing Analysis:")
        print(f"Unique titles: {unique_titles}")
        print(f"Most borrowed book: '{most_borrowed[0]}' with {most_borrowed[1]} days.")
        print(f"Least borrowed book: '{least_borrowed[0]}' with {least_borrowed[1]} days.")
        print(f"Average borrowing duration: {average_days:.2f} days.")
        print("Books sorted by borrowed days (descending):")
        for title, days in sorted_books:
            print(f"  {title}: {days} days")
            



records = [
    "Python Programming - 10",
    "Data Structures - 7",
    "Machine Learning - 15",
    "Python Programming - 5",
    "Artificial Intelligence - 12",
    "Data Structures - 3"
]

task2(records)