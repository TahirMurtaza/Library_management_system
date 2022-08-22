from enum import unique
import json
import requests
from .serializer import CustomSerializerMixin
from ..extensions import db
from datetime import datetime

class Books(db.Model,CustomSerializerMixin):
    __tablename__ = "books"
    serialize_only = ('Id','isbn', 'title', 'authors','avg_rating', 'ratings_count','lang_code','num_pages', 'text_reviews','pub_date','publisher','quantity','polularity')
    Id = db.Column(db.Integer,primary_key=True)
    isbn = db.Column(db.String(50),nullable=False,unique=True)
    title = db.Column(db.String(250),index=True,unique=True)
    authors = db.Column(db.String(250))
    avg_rating = db.Column(db.Float)
    ratings_count = db.Column(db.Integer)
    lang_code = db.Column(db.String(10))
    num_pages = db.Column(db.Integer)
    text_reviews = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime(),default=datetime.utcnow,index=True)
    publisher= db.Column(db.String(250))
    quantity = db.Column(db.Integer,default=10,index=True)
    polularity =db.Column(db.Integer,default=0,index=True)
    
    
    def __init__(self,isbn,title,authors,avg_rating,ratings_count,lang_code,num_pages,text_reviews,pub_date,publisher,quantity,polularity):
        self.isbn = isbn
        self.title = title
        self.authors = authors
        self.avg_rating =  avg_rating      
        self.ratings_count = ratings_count
        self.lang_code = lang_code
        self.num_pages = num_pages 
        self.text_reviews = text_reviews
        self.pub_date = pub_date
        self.publisher= publisher
        self.quantity = quantity
        self.polularity = polularity
        
    def get_all():
        list = []
        items = Books.query.all()
        for item in items:
            list.append(item.to_dict())
        return list
    
    
    def get_frappe_books(title,count):
        page = 1
        if title and count:
            url = f"https://frappe.io/api/method/frappe-library?page=1&title={title}"
        else:
            url = f"https://frappe.io/api/method/frappe-library?page=1"
        res = requests.get(url)
        book_list = []
        book_list = res.json()['message']
        count = int(count)
        if book_list:
            total = len(book_list)
            if total > count:
                reduce = count - total
                book_list = book_list[:reduce]
        return book_list