import os

import pandas as pd

"""
Download data from the urls below and parse into a format ready
to load into our database

This script create a folder for each series
containing a CSV file for each episode
"""

series_urls = (
    "https://taskmaster.fandom.com/wiki/Series_1",
    "https://taskmaster.fandom.com/wiki/Series_2",
    "https://taskmaster.fandom.com/wiki/Series_3",
    "https://taskmaster.fandom.com/wiki/Series_4",
    "https://taskmaster.fandom.com/wiki/Series_5",
    "https://taskmaster.fandom.com/wiki/Champion_of_Champions",
    "https://taskmaster.fandom.com/wiki/Series_6",
    "https://taskmaster.fandom.com/wiki/Series_7",
    "https://taskmaster.fandom.com/wiki/Series_8",
    "https://taskmaster.fandom.com/wiki/Series_9",
    "https://taskmaster.fandom.com/wiki/Series_10",
    "https://taskmaster.fandom.com/wiki/Series_11",
    "https://taskmaster.fandom.com/wiki/Series_12",
    "https://taskmaster.fandom.com/wiki/Series_13",
    "https://taskmaster.fandom.com/wiki/Series_14",
    "https://taskmaster.fandom.com/wiki/Series_15",
    "https://taskmaster.fandom.com/wiki/Series_16",
    "https://taskmaster.fandom.com/wiki/Champion_of_Champions_II",
)
# TODO: parse these in the future. They're not very interesting anyway
ny_urls = (
    # These aren't organized the same as the series
    "https://taskmaster.fandom.com/wiki/Taskmaster%27s_New_Year_Treat#2022",
    "https://taskmaster.fandom.com/wiki/Taskmaster%27s_New_Year_Treat#2021",
    "https://taskmaster.fandom.com/wiki/Taskmaster%27s_New_Year_Treat#2023",
)

for wiki_url_to_parse in series_urls:
    page_name = wiki_url_to_parse.split("/")[-1]
    output_dir = os.path.join("data", page_name)
    os.makedirs(output_dir, exist_ok=True)

    table = pd.read_html(wiki_url_to_parse, attrs={"class": "tmtable"})
    df = table[0]

    inds_table = df[df["Task"].str.contains("Episode")].index
    total_inds = inds_table.to_list() + [len(df) -1]

    for ind1, ind2 in zip(total_inds, total_inds[1:]):
        episode_name = df.iloc[ind1, 0]
        # ind2 is the row for the Total and we can calculate that ourselves
        df_episode = df.iloc[ind1+1: ind2-1]

        # Set disqualified competitors to null
        df_episode = df_episode.replace("DQ", "")

        tie_breaker_row = df_episode["Task"] == "T"
        df_episode[tie_breaker_row] = df_episode[tie_breaker_row].replace({"✔": 1, '✘': 0, "–": ""})
        df_episode.to_csv(f"{output_dir}/{episode_name}.csv", index=False)