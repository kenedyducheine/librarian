import pandas as pd
import requests as req

# use nlp to loop through my ratings and history on good reads to suggest
# a book from either nyt best sellers or goodreads popular books or something else

# nyt csv includes summary of book

## isbn site
# api key = --

## goodreads = test and train
goodreads = pd.read_csv("/Users/KenedyDucheine/PycharmProjects/librarian/goodreads_library_export.csv")
replacedict = {
    '=':'',
    '"':''
}

list1 = [35, 53, 54, 59, 64, 66, 67, 70, 74, 78, 90, 105, 106, 107, 154, 172, 173, 174,
         175, 176, 178, 179]
list2 = [9781784701994, 9781728274898, 9781728274867, 9781778133046, 9781778133008,
         9781668026038, 9780990429272, 9780446561754, 9780307588371, 9781501171345,
         9781945631832, 9780593437834, 9780593437810, 9780525536512, 9780593356159,
         9781503292734, 9781449548636, 9781338878950, 9781526646651, 9780439023528,
         9781804220481, 9780399590528]

## manual isbn entry
for i,j in enumerate(list1):
    goodreads.at[j, 'ISBN13'] = list2[i]

goodreads['ISBN13'] = goodreads['ISBN13'].replace(replacedict, regex=True)
goodreads = goodreads.loc[goodreads['ISBN13']!= "' '"]
goodreads = goodreads.loc[goodreads['ISBN13']!= '']
#rando_space = goodreads.index[goodreads['ISBN13'] == '']
goodreads['ISBN13'] = goodreads['ISBN13'].astype(int)


infolist = []
infodf = pd.DataFrame(columns = ['info'] , index=range(len(goodreads)))
for i in goodreads['ISBN13']:
    h = {'Authorization': '--'}
    url = f"https://api2.isbndb.com/book/{i}"
    resp = req.get(url, headers=h)
    product = resp.json()
    #goodreads['info'] = goodreads['info'].append(product)
    infolist.append(product)
goodreads['info'] = list(infolist)


goodreads = goodreads.reset_index()

# if i just keep the books i have read my training data will literally be 3 objects long
#goodreads = goodreads.loc[goodreads['Read Count'] == 1]

#adding the synopsis to the df
goodreads = goodreads.join(goodreads['info'].apply(pd.Series))
goodreads = goodreads.join(goodreads['book'].apply(pd.Series), how = 'left', lsuffix = 'left', rsuffix='right')
goodreads = goodreads[['Title', 'Author', 'ISBN13', 'My Rating','synopsis']]

goodreads = goodreads.loc[pd.notna(goodreads['synopsis'])]
#goodreads[['My rating']] = goodreads[['My Rating']].replace(0, 1)
#goodreads = goodreads.iloc[:,[0,1,2,4,5,6]]

#goodreads['ISBN13'] = goodreads['ISBN13'].astype(int)


#goodreads['info'] = goodreads['info'].split('synopsis')[1].split('language')[0]

##nyt = irl test
nyt = pd.read_csv('/Users/KenedyDucheine/PycharmProjects/librarian/nyt_bestseller.csv')
nyt = nyt[['isbn13', 'title', 'author', 'description']]
nyt = nyt.dropna(axis = 0)
nyt['isbn13'] = nyt['isbn13'].astype(int)
nyt = nyt[~(nyt['isbn13'].str.contains('A'))]
nyt = nyt[~(nyt['isbn13'].str.contains('B'))]
nyt = nyt[~(nyt['isbn13'].str.contains('D'))]
nyt['isnb13'] = nyt['isbn13'].astype(int)
nyt1 = nyt.iloc[0:4360,]



infolist2 = []
infodf2 = pd.DataFrame(columns = ['info'] , index=range(len(nyt)))
h = {'Authorization': '--'}
for i in nyt1['isbn13']:
    url = f"https://api2.isbndb.com/book/{i}"
    resp = req.get(url, headers=h)
    product = resp.json()
    #goodreads['info'] = goodreads['info'].append(product)
    infolist2.append(product)
nyt1['info'] = list(infolist2)

nyt1 = nyt1.reset_index()
nyt1 = nyt1.join(nyt1['info'].apply(pd.Series))
nyt1 = nyt1.join(nyt1['book'].apply(pd.Series), how = 'left', lsuffix = 'left', rsuffix='right')
nyt1 = nyt1[['titleleft', 'authors', 'isbn13left','synopsis']]
nyt1 = nyt1.loc[pd.notna(nyt1['synopsis'])]






