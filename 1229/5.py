"""
1.class圖書借閱
2.建構子定義
3.屬性(書名 書ID 作者 出版社 出版日期 是否借出 借出日期 還書期限 館藏位置 借書人姓名 學號 email)
4.副函式
"""
class library:
    def __init__(self,library_book,library_id,book_author,book_company,library_date,borrow,borrow_date,due_date,book_location,borrow_name,borrow_id,borrow_email):
        self.library_book = library_book
        self.library_id = library_id
        self.book_author = book_author
        self.book_company = book_company
        self.library_date = library_date
        self.borrow = borrow
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.book_location = book_location
        self.borrow_name = borrow_name
        self.borrow_id = borrow_id
        self.borrow_email = borrow_email

    #l1=library('bookname','12345','作者')
    #print("書名=",l1_library_book)


   
