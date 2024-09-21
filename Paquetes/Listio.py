import numpy as np

def Verify_Iterable_Elements_Of_List(List: list):
    for Element in List:
        if not isinstance(Element, (list, tuple, dict)):
            return False
    return True

def Convert_List_Of_Tuples_To_List_Of_List(Tuples_List: list):
    if Verify_Iterable_Elements_Of_List(Tuples_List):
        Lists_List = []
        for Tuple in Tuples_List:
            Lists_List.append(list(Tuple))
        return Lists_List
    else:
        return list(Tuples_List)

def Find_Max_Position_In_Segment(List: list, Start_Index: int, End_Index: int) -> int:

    '''
    Find the position of the maximum value within a specified segment of a list.

    '''

    Segment = List[Start_Index:End_Index + 1]
    return Segment.index(max(Segment))

def Sort_Lists_By_Reference(Reference_List: list, *Lists_To_Sort: list) -> tuple:

    '''
    Sort a reference list and other associated lists based on the order of the reference list.

    '''

    Current_Index = len(Reference_List) - 1

    while Current_Index > 0:
        Max_Position = Find_Max_Position_In_Segment(Reference_List, 0, Current_Index)
        Reference_List[Max_Position], Reference_List[Current_Index] = Reference_List[Current_Index], Reference_List[Max_Position]
        
        for List in Lists_To_Sort:
            List[Max_Position], List[Current_Index] = List[Current_Index], List[Max_Position]
        
        Current_Index -= 1
        
    return Reference_List, tuple(Lists_To_Sort)

def Calculate_Average_Of_Lists(List_Of_Lists: list) -> list:

    '''
    Calculate the average of each list within a list of lists.

    '''

    Averages = [np.mean(List) for List in List_Of_Lists]
    return Averages

def Transpose_List_Of_Lists(List_Of_Lists: list) -> list:

    '''
    Transpose a list of lists, converting rows to columns and vice versa.

    '''

    Transposed_List = list(map(list, zip(*List_Of_Lists)))
    return Transposed_List

# def Filter_List_By_Criteria() ->  :  
# Función para seleccionar elementos específicos de una lista basada en un criterio.

# def Sort_List() ->  :  
# Función para ordenar una lista de elementos en orden ascendente o descendente.

# def Remove_Duplicates() ->  :  
# Función para eliminar elementos duplicados de una lista, retornando solo valores únicos.

# def Group_Elements() ->  :  
# Función para agrupar elementos en una lista basándose en un criterio específico.

# def Apply_Operation_To_Elements() ->  :  
# Función para aplicar una operación a cada elemento de una lista.

# def Divide_List() ->  :  
# Función para dividir una lista en segmentos de tamaño fijo o basado en un criterio.

# def Concatenate_Lists() ->  :  
# Función para unir múltiples listas en una sola lista.

# def Find_Element() ->  :  
# Función para buscar un elemento en una lista y devolver su índice o una indicación de si existe.

# def Combine_List_With_Function() ->  :  
# Función para combinar elementos de dos listas usando una función específica.

# def Intercalate_List() ->  :  
# Función para intercalar elementos de listas, combinando dos listas alternadamente.

# def Summarize_List() ->  :  
# Función para crear un resumen de una lista de datos, como calcular la media, mediana o desviación estándar de valores numéricos.

# def Generate_List_By_Pattern() ->  :  
# Función para generar una lista siguiendo un patrón específico, como números secuenciales o fechas periódicas.

# def Apply_Function_Iteratively():
# Aplica una función a cada elemento de una lista de manera iterativa, usando el resultado de la función anterior como entrada para la siguiente.

# def Iterate_With_Index():
# Itera sobre los elementos de una lista y proporciona tanto el índice como el valor del elemento en cada iteración.

# def Apply_Transformations():
# Aplica una serie de transformaciones a cada elemento de una lista en un orden específico y devuelve una nueva lista con los resultados.

# def Flatten_Iterables():
# Aplana una lista de iterables (listas, tuplas, etc.) en una sola lista de elementos, eliminando cualquier estructura anidada.

# def Generate_Permutations():
# Genera todas las permutaciones posibles de una lista de elementos y devuelve una lista de todas las combinaciones posibles.

# def Create_Cumulative_List():
# Crea una lista acumulativa donde cada elemento es la suma (o acumulación) de todos los elementos anteriores en la lista original.

def Slice_Iterable_By_Reference(Iterable, Base_Element, Remove = 'Before', Include = True, Appears = 1):

    if Base_Element not in Iterable:
        raise KeyError('The element must be in the iterable.')
    
    Count = 0
    for Index, Element in enumerate(Iterable):
        if Element == Base_Element:
            Count += 1
            if Count == Appears:
                if Remove == 'Before':
                    if Include == False:
                        Index += 1
                    Iterable = Iterable[Index:]
                else:
                    if Include:
                        Index += 1
                    Iterable = Iterable[:Index]
    return Iterable

def Get_Index_Of_All_Ocurrences(Iterable, Target_Element) -> list:
    Count = 1
    Occurrences = []

    for Index, Element in enumerate(Iterable):
        if Element == Target_Element:
            Occurrences.append(Index)
            Count += 1
    
    return Occurrences

def Find_And_Replace(Iterable, Target_Element, New_Value, Occurrence = 1):
    Occurrences_Index = Get_Index_Of_All_Ocurrences(Iterable, Target_Element)
    if Occurrence > len(Occurrences_Index):
        raise KeyError(f"El elemento target {Target_Element} no aparece {Occurrence} veces: aparece menos.")
    
    Index_To_Change = Occurrences_Index[Occurrence - 1]
    Iterable[Index_To_Change] = New_Value
    return Iterable

def Get_Index_Sublist(List, Sublist):
    # Se puede optimizar.
    List_Of_Index = []
    for Index, Element in enumerate(List):
        if Element == Sublist[0]:
            if List[Index:Index+len(Sublist)] == Sublist:
                List_Of_Index.append(Index)
    return List_Of_Index

