# ApiProject
This is a basic Flask project which parses data from nytimes and displays it on a web page. The data can be sorted using a parameter in the request.
The URL is on local host so the call should look something like this: "http://127.0.0.1:5000/news?sort=title_desc" where "sort" is the parameter and "title_desc" is the argument of our call for sorting.
The data can be displayed sorted by title or date and we can also search for a keyword.
