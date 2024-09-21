import pandas as pd
import re
import Stringio
from typing import List, Callable, Optional

def Match_And_Copy_Column_Values(df1: pd.DataFrame, df2: pd.DataFrame, 
                                 Column_df1_A: str, Column_df1_B: str, 
                                 Column_df2_A: str, Column_df2_B: str) -> pd.DataFrame:
    
    '''
    Compare values from df1 and df2 based on Column_df1_A and Column_df2_A, and copy values from Column_df2_B to 
    Column_df1_B in df1.

    '''

    if Column_df1_A == Column_df2_A:
        df2 = df2.rename(columns={Column_df2_A: f"{Column_df2_A}_R"})
        Column_df2_A = f"{Column_df2_A}_R"
    if Column_df1_B == Column_df2_B:
        df2 = df2.rename(columns={Column_df2_B: f"{Column_df2_B}_R"})
        Column_df2_B = f"{Column_df2_B}_R"
    
    for i in range(len(df1)):
        Element_Compared_1 = df1[Column_df1_A][i]
        
        for k in range(len(df2)):
            Element_Compared_2 = df2[Column_df2_A][k]

            if Element_Compared_1 == Element_Compared_2:
                df1.at[i, Column_df1_B] = df2.at[k, Column_df2_B]
    
    return df1

def Compare_Columns(df1: pd.DataFrame, Column1: str, 
                    df2: pd.DataFrame, Column2: str, 
                    Label1: str = "df1", Label2: str = "df2") -> pd.DataFrame:

    '''
    This function compares two specified columns from two separate dataframes and identifies the unique values 
    present in each column but not in the other. It returns a new dataframe with the unique values and the corresponding 
    source of the values (custom labels provided by Label1 and Label2).

    '''

    Column1_Set = set(df1[Column1])
    Column2_Set = set(df2[Column2])
    
    Unique_In_Column1 = Column1_Set - Column2_Set
    Unique_In_Column2 = Column2_Set - Column1_Set
    
    Unique_Values = {
        'Valor': list(Unique_In_Column1) + list(Unique_In_Column2),
        'DataFrame': [Label1] * len(Unique_In_Column1) + [Label2] * len(Unique_In_Column2)
    }
    
    df_Result = pd.DataFrame(Unique_Values)

    pd.set_option('display.max_rows', None)
    
    return df_Result

def Get_Last_Number_Of_String_Column(df: pd.DataFrame, Column_With_Strings: str, New_Column_Name: str) -> pd.DataFrame:
    
    List_Of_Last_Numbers = []
    
    for String in df[Column_With_Strings]:
        Last_List_Of_Last_Numbers = re.findall(r'[\d,]+', String)
        Last_List_Of_Last_Numbers = [float(Character.replace(',', '.')) for Character in Last_List_Of_Last_Numbers]
        List_Of_Last_Numbers.append(Last_List_Of_Last_Numbers)
    
    df[New_Column_Name] = [List[-1] for List in List_Of_Last_Numbers]
    
    return df

def Vertical_Concatenate_For_Multiples_DataFrames(*args) -> pd.DataFrame:
    Mixed = pd.concat(args, ignore_index=True)
    return Mixed

def Fill_Column(df: pd.DataFrame, Column, Value) -> pd.DataFrame:  
    df[Column] = Value
    return df

def Get_Selected_Rows(df: pd.DataFrame, Column: str, Value: object, Condition: str = 'Match') -> pd.DataFrame:

    """
    Filters rows in the DataFrame based on the specified condition applied to a column.

    Conditions supported: 'Match', 'Contains', '>', '<', '>=', '<=', '!=', 'Is in', 'Not in', 'Starts with', 
    'Ends with', 'Is null', 'Is not null', 'Between'.

    """

    if Condition == "Match":
        return df[df[Column] == Value]
    
    elif Condition == "Contains":
        return df[df[Column].str.contains(Value, na=False)]

    elif Condition == ">":
        return df[df[Column] > Value]
    
    elif Condition == "<":
        return df[df[Column] < Value]
    
    elif Condition == ">=":
        return df[df[Column] >= Value]
    
    elif Condition == "<=":
        return df[df[Column] <= Value]
    
    elif Condition == "!=":
        return df[df[Column] != Value]
    
    elif Condition == "Is in":
        if isinstance(Value, (list, set, tuple)):  
            return df[df[Column].isin(Value)]
        else:
            raise ValueError(f"Value for 'Is in' condition must be a list, set, or tuple.")
    
    elif Condition == "Not in":
        if isinstance(Value, (list, set, tuple)):  
            return df[~df[Column].isin(Value)]
        else:
            raise ValueError(f"Value for 'Not in' condition must be a list, set, or tuple.")
    
    elif Condition == "Starts with":
        return df[df[Column].str.startswith(Value, na=False)]

    elif Condition == "Ends with":
        return df[df[Column].str.endswith(Value, na=False)]

    elif Condition == "Is null":
        return df[df[Column].isnull()]

    elif Condition == "Is not null":
        return df[df[Column].notnull()]

    elif Condition == "Between":
        if isinstance(Value, (list, tuple)) and len(Value) == 2:
            return df[df[Column].between(Value[0], Value[1])]
        else:
            raise ValueError(f"Value for 'Between' condition must be a list or tuple with two elements.")

    else:
        raise ValueError(f"Condition '{Condition}' is not supported. Use 'Match', 'Contains', '>', '<', '>=', '<=', '!=', 'Is in', 'Not in', 'Starts with', 'Ends with', 'Is null', 'Is not null', 'Between'.")

def Add_Word_To_Name_Columns(df, Word = None, Separator = '_'):

    if Word == None:
        Word = f'{df}'

    Columns = df.columns.to_list()
    Renaming = {}

    for Column in Columns:
        Renaming[Column] = Stringio.Remove_Acents(Column) + Separator + Word
    
    df.rename(columns=Renaming, inplace=True)

    return df

def Update_Column_Selected_Rows(df: pd.DataFrame, Condition_Column: str, Condition_Value: object, 
                                      Update_Column: str, Update_Value: object, Condition: str) -> pd.DataFrame:
    
    """
    Updates values in a specified column based on a condition applied to another column.

    """

    Filtered_Rows = Get_Selected_Rows(df, Condition_Column, Condition_Value, Condition=Condition)
    df.loc[Filtered_Rows.index, Update_Column] = Update_Value
    return df

def Drop_Selected_Rows(df: pd.DataFrame, Column: str, Value: object, Condition: str) -> pd.DataFrame:

    """
    Drops rows where a specified column meets a certain condition.

    """

    Filtered_Rows = Get_Selected_Rows(df, Column, Value, Condition=Condition)
    df = df.drop(Filtered_Rows.index)
    return df

def Fill_Missing_Values(df: pd.DataFrame, Column: str, Method: str = None, Fill_Value: object = None) -> pd.DataFrame:

    """
    Fills missing values in a specified column using a given method or fill value.

    """

    if Method:
        df[Column] = df[Column].fillna(method=Method)

    elif Fill_Value:
        df[Column] = df[Column].fillna(value=Fill_Value)
    else:
        raise ValueError("Either 'Method' or 'Fill_Value' must be provided.")
    return df

def Apply_Operation_To_Columns(df: pd.DataFrame, Columns: List[str], Operations: Optional[List[Callable]] = None) -> pd.DataFrame:

    """
    Processes specified columns by applying a series of transformations and conversions.

    Example:

    df = Columns_Processing(df,
                            Columns=['Name', 'City', 'Country'],
                            Operations=[lambda x: x.upper(),
                                        Remove_Vocals])

        Upper the text and remove all vocals of these columns.

    """

    for Column in Columns:
        for Operation in Operations:
            df[Column] = df[Column].apply(Operation)
    return df

def Apply_Operations_To_Selected_Rows(df: pd.DataFrame, Filtered_Column: str, Filter_Value: object, Condition: str, 
                                      Columns_To_Operate: List[str], Operations: List[Callable]) -> pd.DataFrame:
    
    """
    Applies a given operations to a list of specified columns for rows filtered by a condition.

    """

    df['Original_Index'] = df.index
    Filtered_Rows = Get_Selected_Rows(df, Filtered_Column, Filter_Value, Condition=Condition)

    for Operation in Operations:
        for Column in Columns_To_Operate:
            df.loc[Filtered_Rows.index, Column] = Filtered_Rows[Column].apply(Operation)

    df = df.sort_values(by='Original_Index').drop(columns='Original_Index').reset_index(drop=True)

    return df

def Find_Best_Value_Column(
    df: pd.DataFrame,
    Target_Column: str,
    Columns_To_Compare: List[str],
    Best_Value_Column: str,
    Comparison_Function: Optional[Callable[[pd.Series, pd.Series], bool]] = None
) -> pd.DataFrame:
    
    """
    Identifies the best value from specified columns based on a comparison function.

    Parameters:
    - df: DataFrame containing the data.
    - Target_Column: The column where the target value is stored.
    - Columns_To_Compare: List of column names to compare against the target value.
    - Best_Value_Column: The name of the column where the best value will be stored.
    - Comparison_Function: Optional function to determine if a value is better. Defaults to equality comparison.
    The function must accept two arguments (the target value and the comparison column value) and return a boolean.

    Returns:
    - The modified DataFrame with the Best_Value_Column updated to the best value based on the comparison function.

    Example:
        df = Find_Best_Value_Column(df,
                                    Target_Column = 'Precio',
                                    Columns_To_Compare = ['Proveedor1', 'Proveedor2', 'Proveedor3'],
                                    Best_Value_Column = 'Mejor_Proveedor',
                                    Comparison_Function = lambda Target, Value: Target == Value
                                    )
    """
    
    if Comparison_Function is None:
        Comparison_Function = lambda Target, Value: Target == Value

    for Index, Row in df.iterrows():
        Best_Value = None
        for Column in Columns_To_Compare:
            if Comparison_Function(Row[Target_Column], Row[Column]):
                Best_Value = Column
                break
        df.at[Index, Best_Value_Column] = Best_Value if Best_Value is not None else pd.NA

    return df

def Convert_Type_Of_Columns(df: pd.DataFrame, List_Of_Columns: list, Type = str):
    for Column in List_Of_Columns:
        if Column in df.columns:
            if df[Column].dtype != Type:
                df[Column] = df[Column].astype(Type)
    return df

def Casing_Column_Names(df: pd.DataFrame, Style: str = 'Upper Snake Case') -> pd.DataFrame:
    Columns = list(df.columns)
    if Style == 'Camel Case':
        Columns = [Stringio.Apply_Camel_Case(str(Column)) for Column in Columns]
    elif Style == 'Snake Case':
        Columns = [Stringio.Apply_Snake_Case(str(Column)) for Column in Columns]
    elif Style == 'Upper Snake Case':
        Columns = [Stringio.Apply_Upper_Snake_Case(str(Column)) for Column in Columns]
    elif Style == 'Screaming Snake Case':
        Columns = [Stringio.Apply_Screaming_Snake_Case(str(Column)) for Column in Columns]
    elif Style == 'Pascal Case':
        Columns = [Stringio.Apply_Pascal_Case(str(Column)) for Column in Columns]
    
    df.columns = Columns
    return df

def Change_Column_Names_By_Dictionary(df: pd.DataFrame, Dictionary: dict) -> pd.DataFrame:
    return df.rename(columns=Dictionary)








