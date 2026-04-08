# Simple movie recommendation system

movies = {
    "action": ["Avengers", "Batman", "Iron Man"],
    "comedy": ["Mr. Bean", "The Mask", "Home Alone"],
    "horror": ["Conjuring", "Annabelle", "Insidious"],
    "romance": ["Titanic", "Notebook", "La La Land"]
}

print("Movie Categories: action, comedy, horror, romance")
choice = input("Enter your favorite category: ").lower()

if choice in movies:
    print("Recommended movies:")
    for movie in movies[choice]:
        print("-", movie)
else:
    print("Sorry, category not found.")
