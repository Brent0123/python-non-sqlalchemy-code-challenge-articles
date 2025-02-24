# lib/classes/many_to_many.py
class Article:
    # Class-level list to track all Article instances (single source of truth)
    all = []

    def __init__(self, author, magazine, title):
        """Initialize an Article with an Author, Magazine, and title.
        
        Args:
            author: An instance of Author
            magazine: An instance of Magazine
            title: A string title for the article (5-50 characters)
        
        Raises:
            Exception: If title is not a string, or not between 5 and 50 characters,
                      or if author/magazine are not of the correct type.
        """
        # Validate author is an instance of Author
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        
        # Validate magazine is an instance of Magazine
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine class")
        
        # Validate title is a string and within length constraints
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be between 5 and 50 characters inclusive")
        
        # Set immutable properties using private attributes
        self._title = title
        self._author = author
        self._magazine = magazine
        
        # Add this article to the class-level list
        Article.all.append(self)

    @property
    def title(self):
        """Return the article's title (immutable, read-only).
        
        Returns:
            str: The article title
            
        Raises:
            Exception: If attempting to modify (handled by Python's property behavior).
        """
        return self._title

    @property
    def author(self):
        """Return or set the article's author (mutable).
        
        Returns:
            Author: The article's author
            
        Raises:
            Exception: If the new author is not an instance of Author.
        """
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise Exception("Author must be an instance of Author class")
        self._author = new_author

    @property
    def magazine(self):
        """Return or set the article's magazine (mutable).
        
        Returns:
            Magazine: The article's magazine
            
        Raises:
            Exception: If the new magazine is not an instance of Magazine.
        """
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine class")
        self._magazine = new_magazine


class Author:
    # Class-level list to track all Author instances
    all = []

    def __init__(self, name):
        """Initialize an Author with a name.
        
        Args:
            name: A string name longer than 0 characters
            
        Raises:
            Exception: If name is not a string or is empty.
        """
        # Validate name is a string and longer than 0 characters
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) <= 0:
            raise Exception("Name must be longer than 0 characters")
        
        # Set immutable name using private attribute
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        """Return the author's name (immutable, read-only).
        
        Returns:
            str: The author's name
        """
        return self._name

    def articles(self):
        """Return a list of all articles written by this author.
        
        Returns:
            list: List of Article instances associated with this author
        """
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        """Return a unique list of magazines this author has contributed to.
        
        Returns:
            list: Unique list of Magazine instances
        """
        # Use set to ensure uniqueness, then convert back to list
        unique_magazines = set(article.magazine for article in self.articles())
        return list(unique_magazines)

    def add_article(self, magazine, title):
        """Create and return a new Article instance for this author with the given magazine and title.
        
        Args:
            magazine: A Magazine instance
            title: A string title for the article
            
        Returns:
            Article: The newly created Article instance
            
        Raises:
            Exception: If magazine is not an instance of Magazine.
        """
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine class")
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        """Return a unique list of magazine categories (topic areas) this author has contributed to.
        
        Returns:
            list: Unique list of category strings, or None if no articles
        """
        if not self.articles():
            return None
        unique_categories = set(article.magazine.category for article in self.articles())
        return list(unique_categories)


class Magazine:
    # Class-level list to track all Magazine instances
    all = []

    def __init__(self, name, category):
        """Initialize a Magazine with a name and category.
        
        Args:
            name: A string name between 2 and 16 characters
            category: A string category longer than 0 characters
            
        Raises:
            Exception: If name/category is not a string, or if name/category does not meet length constraints.
        """
        # Validate name is a string and between 2 and 16 characters
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if not (2 <= len(name) <= 16):
            raise Exception("Name must be between 2 and 16 characters inclusive")
        
        # Validate category is a string and longer than 0 characters
        if not isinstance(category, str):
            raise Exception("Category must be a string")
        if len(category) <= 0:
            raise Exception("Category must be longer than 0 characters")
        
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        """Return or set the magazine's name (mutable).
        
        Returns:
            str: The magazine's name
        """
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise Exception("Name must be a string")
        if not (2 <= len(new_name) <= 16):
            raise Exception("Name must be between 2 and 16 characters inclusive")
        self._name = new_name

    @property
    def category(self):
        """Return or set the magazine's category (mutable).
        
        Returns:
            str: The magazine's category
        """
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise Exception("Category must be a string")
        if len(new_category) <= 0:
            raise Exception("Category must be longer than 0 characters")
        self._category = new_category

    def articles(self):
        """Return a list of all articles published by this magazine.
        
        Returns:
            list: List of Article instances associated with this magazine
        """
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        """Return a unique list of authors who have written for this magazine.
        
        Returns:
            list: Unique list of Author instances
        """
        unique_authors = set(article.author for article in self.articles())
        return list(unique_authors)

    def article_titles(self):
        """Return a list of title strings for all articles in this magazine.
        
        Returns:
            list: List of title strings, or None if no articles
        """
        articles_list = self.articles()
        if not articles_list:
            return None
        return [article.title for article in articles_list]

    def contributing_authors(self):
        """Return a list of authors who have written more than 2 articles for this magazine.
        
        Returns:
            list: List of Author instances with > 2 articles, or None if no such authors
        """
        author_counts = {}
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        
        prolific_authors = [author for author, count in author_counts.items() if count > 2]
        return prolific_authors if prolific_authors else None

    @classmethod
    def top_publisher(cls):
        """Return the Magazine instance with the most articles.
        
        Returns:
            Magazine: The magazine with the most articles, or None if no articles exist
        """
        if not Article.all:
            return None
        
        magazine_counts = {}
        for article in Article.all:
            magazine = article.magazine
            magazine_counts[magazine] = magazine_counts.get(magazine, 0) + 1
        
        if not magazine_counts:
            return None
        
        # Find the magazine with the most articles
        top_magazine = max(magazine_counts.items(), key=lambda x: x[1])[0]
        return top_magazine