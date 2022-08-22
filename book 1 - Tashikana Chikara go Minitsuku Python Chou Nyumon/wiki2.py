import requests, sys, codecs
search_word = sys.argv[1]
api_url='https://zh.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm', 'action':'query', 'prop':'revisions', 'rvprop':'content'}
api_params['titles'] = search_word
wiki_data = requests.get(api_url,params=api_params)
fo = codecs.open('C:\\Users\\HP\\Desktop\\py_folder\\' + search_word + '.html','w','utf-8')
fo.write(wiki_data.text)
fo.close()