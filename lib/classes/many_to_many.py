class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = None
        self.title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not hasattr(self, '_title') or self._title is None:
            if isinstance(value, str) and 5 <= len(value) <= 50:
                self._title = value
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        self._magazine = value


class Author:
    def __init__(self, name):
        self._name = None
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not hasattr(self, '_name') or self._name is None:
            if isinstance(value, str) and len(value) > 0:
                self._name = value
          
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        magazines = []
        seen = set()  
        for article in self.articles():
            if article.magazine not in seen:
                magazines.append(article.magazine)
                seen.add(article.magazine)
        return magazines

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        areas = []
        seen = set() 
        for article in self.articles():
            category = article.magazine.category
            if category not in seen:
                areas.append(category)
                seen.add(category)
        return areas


   

class Magazine:
      all = []
    
      def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        Magazine.all.append(self)
    
      @property
      def name(self):
        return self._name
    
      @name.setter
      def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
      @property
      def category(self):
        return self._category
    
      @category.setter
      def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

      def articles(self):
        return [article for article in Article.all if article.magazine == self]

      def contributors(self):
        authors = []
        seen = set()
        for article in self.articles():
            if article.author not in seen:
                authors.append(article.author)
                seen.add(article.author)
        return authors

      def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

      def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        
        authors = [author for author, count in author_counts.items() if count > 2]
        return authors if authors else None
    
      @classmethod
      def top_publisher(cls):
        if not Article.all:
            return None
        
        magazine_counts = {}
        for article in Article.all:
            magazine = article.magazine
            magazine_counts[magazine] = magazine_counts.get(magazine, 0) + 1
        
        return max(magazine_counts, key=magazine_counts.get)