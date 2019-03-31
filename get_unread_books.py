#!/usr/bin/env python
#
# Copyright (c) 2019 Maria Bornski
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

# Standard library modules
import argparse

# Non-standard modules, need to acquire and set up correctly.
import lector

def get_unread_books(amazon_username, amazon_password, unread_percentage):
    unread_books = []
    try:
        api = lector.KindleCloudReaderAPI(amazon_username, amazon_password)
    except Exception as e:
        print(e)
        exit(1)
    my_library = api.get_library_metadata()
    for book in my_library:
        book_progress = api.get_book_progress(book.asin)
        _, current_page, last_page = book_progress.page_nums
        # Calculate unread percentage as current page divide by last page
        this_book_percentage = ((current_page / last_page) * 100) 
        if this_book_percentage <= unread_percentage:
            unread_books.append((book, unread_percentage))
    return unread_books

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--amazon_username", help="Your Amazon username for the kindle account you want data for")
    parser.add_argument("-p", "--amazon_password", help="Your Amazon password for the kindl account you want data for")
    parser.add_argument("--unread_percentage", type=int, help="The max unread percentage you want to know about.  Books with a higher unread percentage won't be listed")
    args = parser.parse_args()

    uread_books = get_unread_books(args.amazon_username, args.amazon_password, args.unread_percentage)
    print(unread_books)

if __name__ == "__main__":
    main()
