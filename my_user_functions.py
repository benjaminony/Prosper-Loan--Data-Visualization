import numpy as np
from IPython.display import display_html

def print_shape(df):
    """Displays formatted number of rows and columns in dataframe
    
    Arguments:
        df: dataframe
    Return:
        None
    """
    print('Dataframe has {} rows and {} columns'.
          format(df.shape[0], df.shape[1]))
    
def print_frequency(df, col):
    """Displays the frequency of each unique value in dataframe column
    
    Arguments:
        df: dataframe
        col: (string) name of column in dataframe
    Return:
        None
    """
    print('Frequency of each unique value in column:\n', df[col].value_counts())

    
def print_unique(df, col):
    """Prints fromatted, not null unique entries in dataframe (df) column (col)
    Arguments:
        df: dataframe
        col: (string) column name
    """
    unique_list = df[col].unique()
    print('{} column, {} unique entries:'.format(col, unique_list.shape[0]))
    for i in unique_list:
        print('- ', i)
    
    
def data_overview(df):
    """Prints shape, column dtypes, head and descriptive statistics for dataframe (df)
    
    Arguments:
        df: Dataframe
    Return:
        None
    """
    print_shape(df)
    print('\nDtypes:')
    print(df.dtypes)
    print('\nHead:')
    display_html(df.head())
    print('\nDescribe:')
    display_html(df.describe())
        
    
def download_file(url):
    """downloads file using url and
    saves file to folder using document name and extension
    
    Arguments:
        url: file url
    Return:
        none
    """
    response = requests.get(url)
    with open(url.split('/')[-1], mode='wb') as file:
        file.write(response.content)

        
def check_duplicates(df, columns):
    """checks coloumns in dataframe (df) for duplicates
    and prints the sum of duplicates
    
    Arguments:
        df: dataframe
        columns: list of df column names to check
    Returns:
        None
    """
    for col in columns:
        print('{} column duplicates: {}\n'.format(col, sum(df[col].duplicated())))
        

def root_transform(x, root, inverse = False):
    """square and cube root transformation helper
    
    Arguments:
        x: integer to get root
        root: (string) square or cube
        inverse: (bool) True, to invert root
    Return:
        (scaler) root or invert root of x
    """
    if not inverse:
        if root == 'square':
            return np.sqrt(x)
        if root == 'cube':
            return np.cbrt(x)
    else:
        if root == 'square':
            return x ** 2
        if root == 'cube':
            return x ** 3
        

def has_fraction(num_list):
    """Checks if numeric list contains fraction
    
    Arguments:
        num_list: list of numbers
    Return:
        Bool: True or False
    """
    for x in num_list:
        if (x != None):
            if (x//1 != x/1):
                return True
    return False


def find_key_once(input_dict, value):
    for key, values in input_dict.items():
        for v in values:
            if v == value:
                return key
                break
    if v:
        return 'None'


def annot_countplot(axis, hu = 0, vr = 0):
    """Annotate countplot bars
    
    Arguments:
        axis: plot axis on figure object
        hu: horizontal move up
        vr: vertical move right
    Returns:
        None
    """
    for p in axis.patches:
        axis.annotate('{}'.format(p.get_height()), (p.get_x()+hu, p.get_height()+vr))

    
def get_fico(x):
    """Takes in a number and returns it's FICO model group name
    
    Arguments:
        x = number
    Returns:
        (string) Poor | Fair | Good | Very Good | Exceptional
    """
    if x <= 299.0:
        return None
    elif (x <= 579.0):
        return 'Poor'
    elif (x <= 669.0):
        return 'Fair'
    elif (x <= 739.0):
        return 'Good'
    elif (x <= 799.0):
        return 'Very Good'
    elif (x <= 850.0):
        return 'Exceptional'
    else:
        return None