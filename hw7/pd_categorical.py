"""
Load following survey data into a Pandas dataframe called x and note that the top part of the Is there anything in particular you want to use Python for? column looks like the following,

Is there anything in particular you want to use Python for?
ID
3931	Data extraction and processing, Data analytics...
4205	Data extraction and processing
3669	Data analytics, Machine learning, Statistical ...
1452	Data extraction and processing, Data analytics...
2968	Numerical processing, Data analytics, Machine ...
The problem with this column is that there are multiple comma-separated values in it. Please write a Python function called split_count that can take this column as input and output the following Pandas dataframe.

count
All of the above	1
Computer vision	1
Image Processing	1
Computer vision/image processing	1
As a general skill	1
scripting seems desirable for many jobs	1
not sure	1
Computer Vision	1
EDA tools	1
Web development	104
Numerical processing	173
Scientific visualization	198
Statistical analysis	222
Data extraction and processing	291
Data analytics	351
Machine learning	381
Here is the function signature: split_count(x) where x is a pd.Series object and it returns a pd.DataFrame object.
"""
import pandas as pd
import pandas.api.types as ptypes
from collections import Counter
import calendar


def split_count(series):
    """
    Does the thingy
    :param series:
    :type series:
    :return:
    :rtype:
    """
    assert isinstance(series, pd.Series)
    assert ptypes.is_string_dtype(series)

    things = []
    for thing in series:
        things.extend(thing.split(', '))
    c = Counter(things)
    df = pd.DataFrame(c.most_common())
    df = df.set_index(0)
    df = df.sort_values(by=1)
    df.index.name = None
    df = df.rename(columns={1: "count"})
    return df


def add_month_yr(df):
    """
    Earth, water, fire, air. Long ago, the four nations lived in harmony. Then
    everything changed when the fire nation attacked.
    :param series:
    :type series:
    :return:
    :rtype:
    """

    assert isinstance(df, pd.DataFrame)
    assert "Quarter" in df.columns


    def replace(thing):
        month, day, year = thing.split(" ")[0].split("/")
        month_name = calendar.month_name[int(month)]
        return month_name[:3] + "-" + year

    series = pd.Series( [replace(thing) for thing in df["Timestamp"]])  #, index=list(df["ID"])
    # return series
    df["month-yr"] = series
    return df


def count_month_yr(x):
    """
    100 years passed and my brother and I discovered the new avatar, Aang. And although
    his airbending skills are great, he has a lot to learn before he's ready to save anyone.
    :param x:
    :type x:
    :return:
    :rtype:
    """
    df = add_month_yr(x)
    series = df.groupby("month-yr").size()
    df = pd.DataFrame(series, columns=["Timestamp"])
    return df


def fix_categorical(x):
    """
    But I believe Aang can save the world
    :param x:
    :type x:
    :return:
    :rtype:
    """
    # assert isinstance(x, pd.DataFrame)
    # assert "month-yr" in x.columns
    # assert set(x["month-yr"]) == {'Jan-2018', 'Mar-2018', 'Feb-2018', 'Jan-2019', 'Sep-2017', 'Sep-2018', 'Oct-2018', 'Apr-2018'}
    df = add_month_yr(x)
    df["month-yr"] = pd.Categorical(df["month-yr"], ordered=True, categories=["Sep-2017", "Jan-2018", "Feb-2018", "Mar-2018", "Apr-2018", "Sep-2018", "Oct-2018", "Jan-2019"])
    df.groupby('month-yr')['Timestamp'].count().to_frame().sort_index()
    # df.groupby('month-yr')['Timestamp'].count().to_frame().sort_index()
    return df


if __name__ == '__main__':
    data = pd.read_csv("survey_data.csv")
    col = data["Is there anything in particular you want to use Python for?"]
    df = add_month_yr(data)
    # print(df["month-yr"])
    # print(df.head())
    df = fix_categorical(df)
