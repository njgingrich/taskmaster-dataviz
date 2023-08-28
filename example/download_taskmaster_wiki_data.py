import sys

import pandas as pd

"""
Example usage:
    src/download_taskmaster_wiki_data.py https://taskmaster.fandom.com/wiki/Series_1

This will create a CSV file for each episode on the page.
"""

wiki_url_to_parse = sys.argv[1]
table = pd.read_html(wiki_url_to_parse, attrs={"class": "tmtable"})
df = table[0]

inds_table = df[df["Task"].str.contains("Episode")].index
total_inds = inds_table.to_list() + [len(df) -1]

for ind1, ind2 in zip(total_inds, total_inds[1:]):
    episode_name = df.iloc[ind1, 0]
    # ind2 is the row for the Total and we can calculate that ourselves
    df_episode = df.iloc[ind1+1: ind2-1]
    df_episode.to_csv(f"{episode_name}.csv", index=False)
