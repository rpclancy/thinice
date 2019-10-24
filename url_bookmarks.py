import webbrowser

"""
Opens various urls in browser. Using to store and access thinice resources.
Add new urls to URL list below.
Run from terminal using: python url_bookmarks.py
"""

###### URL LIST #######

# Github repository
urls = ['https://github.com/rpclancy/thinice_repo']
#
urls.append('')
#
#urls.append('')
#
#urls.append('')

###### Open URLS #######
for url in urls: 
    webbrowser.open(url, new=1)

print('Done')