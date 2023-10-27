from src.dependencies import *
def combine_dataframes(dfs):
    """The combine_dataframes function takes a list of dataframes as input and concatenates them into a single dataframe.

    Args:

    dfs: a list of pandas dataframes to be combined
    Returns:

    combined_df: a single pandas dataframe with all the rows from the input dataframes
    The function iterates through each dataframe in the input list,
    and uses the append() method to concatenate it to the previously combined dataframe.
    It also sets ignore_index=True to ensure that the row indexes are reset in the final dataframe.
    Finally, it returns the concatenated dataframe."""
    combined_df = pd.DataFrame()  # create an empty dataframe to start with
    for df in dfs:
        combined_df = combined_df.append(df, ignore_index=True)  # append the rows of the current dataframe to the previous one
    return combined_df

def skew_kurt(data, col):
    """
    Calculate the skewness and kurtosis of a given column in a dataset.
    
    Parameters:
        data (DataFrame): The dataset containing the column.
        col (str): The name of the column to calculate the skewness and kurtosis for.
        
    Returns:
        None
    """
    
    # Calculate skewness and kurtosis of Income column
    _skewness = skew(data[col])
    _kurtosis = kurtosis(data[col])

    # Create histogram of Income column with mean, median, and mode
    sns.histplot(data=data, x=col, kde=True)
    plt.axvline(data[col].mean(), color='r', linestyle='--', label='Mean')
    plt.axvline(data[col].median(), color='g', linestyle='--', label='Median')
    plt.axvline(data[col].mode()[0], color='b', linestyle='--', label='Mode')
    plt.legend()

    # Add text annotation for skewness and kurtosis values
    plt.annotate('Skewness: {:.2f}'.format(_skewness), xy=(0.5, 0.9), xycoords='axes fraction')
    plt.annotate('Kurtosis: {:.2f}'.format(_kurtosis), xy=(0.5, 0.85), xycoords='axes fraction')

    plt.show()