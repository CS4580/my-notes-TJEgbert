"""_KNN Analysis of Movies
"""
import pandas as pd
import numpy as np
import get_data as gt

# Constants
K = 10  # number of closes matches
BASE_CASE_ID = 88763  # IMDB_id for 'Back to the Future'
SECOND_CASE_ID = 89530  # IMDB id for 'Mad Max'
BASE_YEAR = 1985


def metric_stub(base_case_value, comparator_value):
    return 0


def print_top_k(df, sorted_value, comparison_type):
    print(f'Top {K} closest matches by {comparison_type}')
    counter = 1
    for idx, row in df.head(K).iterrows():
        print(f"""Top {counter} match: [{idx}]:{row['year']} {row['title']}, {
              row['genres']}, [{row[sorted_value]}]""")
        counter += 1


def euclidean_distance(base_case_year: int, comparator_year: int):
    return abs(base_case_year - comparator_year)


def jaccard_similarity_normal(base_case_genres: str, comparator_genres: str):
    base_genres_set = set(base_case_genres.split(';'))
    comparator_genres_set = set(comparator_genres.split(';'))
    numerator = len(base_genres_set.intersection(comparator_genres_set))
    denominator = len(base_genres_set.union(comparator_genres_set))
    return float(numerator)/float(denominator)


def _get_weighted_jarracd_simmilarity_dictionary(df):
    # Get our selection of our BASE_CASE_ID and SECOND_CASE_ID
    selections_df = [df.loc[BASE_CASE_ID], df.loc[SECOND_CASE_ID]]
    # ADD weights for the similarity index
    genres_weighted_dictionary = {'total': 0}
    for movie in selections_df:
        for genre in movie['genres'].split(';'):
            if genre in genres_weighted_dictionary:
                genres_weighted_dictionary[genre] += 1
            else:
                genres_weighted_dictionary[genre] = 1
            genres_weighted_dictionary['total'] += 1
    return genres_weighted_dictionary


def jaccard_similarity_weighted(df: pd.DataFrame, comparator_genre: str):
    weighted_dictionary = _get_weighted_jarracd_simmilarity_dictionary(df)
    numerator = 0
    denominator = weighted_dictionary['total']
    for genre in comparator_genre.split(';'):
        if genre in weighted_dictionary:
            numerator += weighted_dictionary[genre]
    return float(numerator)/float(denominator)


def knn_analysis_driver(data_df, base_case, comparison_type, metric_func, sorted_value='metric'):
    # WIP: Create df of filter data
    df = data_df.copy()  # Makes a copy of the dataframe

    if metric_func.__name__ == 'jaccard_similarity_weighted':
        df[sorted_value] = df[comparison_type].map(
            # Uses the  input function and passes parementers here
            lambda x: metric_func(df, x))
    else:
        df[sorted_value] = df[comparison_type].map(
        # Uses the  input function and passes parementers here
            lambda x: metric_func(base_case[comparison_type], x))
    
    # Sort return values fromm function stub
    # jaccard needs to be sorting decending
    if 'jaccard' in metric_func.__name__:
        sorted_df = df.sort_values(by=sorted_value, ascending=False)
    else:
        # default is ascending = True
        sorted_df = df.sort_values(by=sorted_value)
    sorted_df.drop(BASE_CASE_ID, inplace=True)  # drop base case
    # print(sorted_df['title'].head(K)) # Top ten values
    print_top_k(sorted_df, sorted_value, comparison_type)


def main():
    # TASK 1: Get dataset from server
    print(f'\nTask 1: Download dataset from server')
    dataset_file = 'movies.csv'
    gt.download_dataset(gt.ICARUS_CS4580_DATASET_URL, dataset_file)
    # TASK 2: Load  data_file into a DataFrame
    print(f'\nTask 2: Load IMDB data into a DataFrame')
    data_file = f'{gt.DATA_FOLDER}/{dataset_file}'
    data = gt.load_data(data_file, index_col='IMDB_id')
    print(f'Loaded {len(data)} records')
    print(f'Data set Columns {data.columns}')
    print(f'Data set description {data.describe()}')
    # Task 3: KNN Analysis Driver
    print(f'\nTask 3: KNN Simple Analysis')
    base_case = data.loc[BASE_CASE_ID]
    print(f'Comparing all movies to our case: {base_case['title']}')
    # Don't pass in parameters when passing in function
    knn_analysis_driver(data_df=data, base_case=base_case,
                        comparison_type='genres', metric_func=metric_stub, sorted_value='metric')

    # Task 4: Euclidean Distance based on Year
    print(f'\nTask 4: KNN Analysis with Euclidean Distance')
    knn_analysis_driver(data_df=data, base_case=base_case,
                        comparison_type='year', metric_func=euclidean_distance, sorted_value='euclidean_distance')

    # Task 5: Jaccard Similarity
    print(f'\nTask 5: KNN Analysis with Jarracrd Similarity Normal')
    data = data[data['year'] >= BASE_YEAR]  # filter
    knn_analysis_driver(data_df=data, base_case=base_case,
                        comparison_type='genres', metric_func=jaccard_similarity_normal, sorted_value='jaccard_similarity')

    # Task 6: Jaccard Weighted Similarity
    print(f'\nTask 6: KNN Analysis with Jarracrd Similarity Weighted')
    base_case = data.loc[BASE_CASE_ID]
    second_case = data.loc[SECOND_CASE_ID]
    print(f'Comparing all to our base case: [{base_case['title']}] and second case:{second_case['title']}')
    # Add a second filter: rating ['G','PG','PG-13']
    # Add a third filterL stars >= 5
    data = data[data['year'] >= BASE_YEAR]  # filter
    data = data[(data['stars'] >= 5) & (data['rating'].isin(['G', 'PG', 'PG-13']))] # Starts and rating filter
    knn_analysis_driver(data_df=data, base_case=base_case,
                        comparison_type='genres', metric_func=jaccard_similarity_weighted, sorted_value='jaccard_similarity_weighted')


if __name__ == '__main__':
    main()
