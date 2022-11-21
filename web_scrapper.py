 # %%

import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools


# our search term, using syntax for Twitter's Advanced Search
search = '"data science"'

# the scraped tweets, this is a generator
scraped_tweets = sntwitter.TwitterSearchScraper(search).get_items()

# slicing the generator to keep only the first 100 tweets
sliced_scraped_tweets = itertools.islice(scraped_tweets, 100)

# convert to a DataFrame and keep only relevant columns
df = pd.DataFrame(sliced_scraped_tweets)[['date', 'content']]

pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
    '"data science"').get_items(), 100))
# %%
loc = '21.17429, -86.84656, 50km'
df_coord = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
    'seguridad covid cancun'+' since:2020-03-03 until:2022-12-18').get_items(), 1000))[['user', 'date','content']]

df_coord['user_location'] =  df_coord['user'].apply(lambda x: x['location'])
df_coord
# %%
df_english = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
    'tourism'+' recovery'+' since:2020-01-01 until:2022-08-08').get_items(), 1000))[['user', 'date','content']]

df_english['user_location'] =  df_english['user'].apply(lambda x: x['location'])
df_english
# %%
