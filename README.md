# forager

A search engine to search gourmet food reviews data and return the top K
reviews that have the highest overlap with the input query.

# execute
virtualenv -p python3 venv  
pip install -r requirements.txt  
flask run
  
http://127.0.0.1:5000/search?search=all  
It will return all the documents having term 'all'