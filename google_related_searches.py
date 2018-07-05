import mechanize
import re



def get_related_searches(query):
    """
    Method to return list of related queries searched by user for given google search query

    Args:
        query (str): query string

    Return:
        (list): 
    """
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0')] 
    br.open('http://www.google.com/')   
    br.select_form(name='f')   
    br.form['q'] = query
    data = br.submit()
    related_query = re.findall('\"rfs\"\\:\\[(.*)\\]', data.read())
    related_query = related_query[0].split(',')
    related_searches = [x.replace('"','') for x in related_query]
    return related_searches
