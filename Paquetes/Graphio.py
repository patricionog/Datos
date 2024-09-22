import matplotlib.pyplot as plt
import seaborn as sns

#######################################################################################################################
# CREATE #
#######################################################################################################################

def Create_Line_Plot(X, Y, Title = None, X_Label = 'X', Y_Label = 'Y', Color = 'blue', Grid = True, Figure_Size = (10, 6), 
                     Font_Size = 12, Alpha = 1.0):
    
    plt.figure(figsize=Figure_Size)
    plt.plot(X, Y, color = Color, marker = 'o', alpha = Alpha)
    if Title:
        plt.title(Title, fontsize=Font_Size)
    plt.xlabel(X_Label, fontsize=Font_Size)
    plt.ylabel(Y_Label, fontsize=Font_Size)
    if Grid:
        plt.grid(True)
    plt.show()

def Create_Histogram(Data, Title = None, X_Label = 'X', Y_Label = 'Y', Bins = 10, Color = 'blue', Alpha = 0.7, 
                     Grid = True, Figure_Size = (10, 6), Font_Size = 12):
    
    plt.figure(figsize=Figure_Size)
    plt.hist(Data, bins = Bins, color = Color, alpha = Alpha)
    if Title:
        plt.title(Title, fontsize=Font_Size)
    plt.xlabel(X_Label, fontsize=Font_Size)
    plt.ylabel(Y_Label, fontsize=Font_Size)
    if Grid:
        plt.grid(True)
    plt.show()

def Create_Bar_Plot(Categories, Values, Title = None, X_Label = 'X', Y_Label = 'Y', Color = 'blue', Grid = True, Figure_Size = (10, 6), 
                    Font_Size = 12, Orientation = 'vertical'):
    
    plt.figure(figsize=Figure_Size)
    if Orientation == 'horizontal':
        plt.barh(Categories, Values, color = Color)
    else:
        plt.bar(Categories, Values, color = Color)
        
    if Title:
        plt.title(Title, fontsize=Font_Size)
    plt.xlabel(X_Label, fontsize=Font_Size)
    plt.ylabel(Y_Label, fontsize=Font_Size)
    if Grid:
        plt.grid(axis='y')
    plt.show()

def Create_Box_Plot(Data, Title = None, X_Label = 'X', Y_Label = 'Y', Grid = True, Figure_Size = (10, 6), Font_Size = 12):
    
    plt.figure(figsize=Figure_Size)
    sns.boxplot(data = Data)
    if Title:
        plt.title(Title, fontsize=Font_Size)
    plt.xlabel(X_Label, fontsize=Font_Size)
    plt.ylabel(Y_Label, fontsize=Font_Size)
    if Grid:
        plt.grid(True)
    plt.show()

def Create_Scatter_Plot_With_Regression(X, Y, Title = None, X_Label = 'X', Y_Label = 'Y', Color = 'blue', Grid = True, Figure_Size = (10, 6), 
                                         Font_Size = 12, Alpha = 1.0):
    
    plt.figure(figsize=Figure_Size)
    sns.regplot(x = X, y = Y, scatter_kws = {'color': Color, 'alpha': Alpha}, 
                line_kws = {'color': 'red'})
    if Title:
        plt.title(Title, fontsize=Font_Size)
    plt.xlabel(X_Label, fontsize=Font_Size)
    plt.ylabel(Y_Label, fontsize=Font_Size)
    if Grid:
        plt.grid(True)
    plt.show()

def Create_Violin_Plot(Data, Title = None, X_Label = 'X', Y_Label = 'Y', 
                       Grid = True, Figure_Size = (10, 6), Font_Size = 12):
    
    plt.figure(figsize=Figure_Size)
    sns.violinplot(data = Data)
    if Title:
        plt.title(Title, fontsize=Font_Size)
    plt.xlabel(X_Label, fontsize=Font_Size)
    plt.ylabel(Y_Label, fontsize=Font_Size)
    if Grid:
        plt.grid(True)
    plt.show()

#######################################################################################################################
# GROUP #
#######################################################################################################################

# No está bien hecha.
def Create_Subplots(Plot_Functions, Titles = None, Rows = 1, Columns = 1, Figure_Size = (15, 10), Shared_X_Axis = False, Shared_Y_Axis = False):

    """
    Creates a grid of subplots and applies specified plotting functions to each subplot.

    Parameters:
        - Plot_Functions (list of callable): List of functions to generate plots.
        - Titles (list of str, optional): Titles for each subplot. Default is None.
        - Rows (int, optional): Number of rows in the subplot grid. Default is 1.
        - Columns (int, optional): Number of columns in the subplot grid. Default is 1.
        - Figure_Size (tuple, optional): Size of the figure in inches. Default is (15, 10).
        - Shared_X_Axis (bool, optional): If True, share the x-axis among subplots. Default is False.
        - Shared_Y_Axis (bool, optional): If True, share the y-axis among subplots. Default is False.

    Example:
        def Sample_Plot(Title=None):
            plt.plot([1, 2, 3], [4, 5, 6])
            if Title:
                plt.title(Title)

        Create_Subplots(
            Plot_Functions=[lambda Title: Create_Line_Plot(X, Y1, Title=Title),
                            lambda Title: Create_Histogram(Y2, Title=Title)],
            Titles=['First Plot', 'Second Plot'],
            Rows=1,
            Columns=2)

    """

    Figure, Axis_List = plt.subplots(nrows = Rows, ncols = Columns, figsize = Figure_Size, sharex = Shared_X_Axis, sharey = Shared_Y_Axis)
    
    for Index, Plot_Function in enumerate(Plot_Functions):
        Axis = Axis_List[Index // Columns, Index % Columns] if Rows > 1 else Axis_List[Index]
        plt.sca(Axis)
        
        if Titles and Index < len(Titles):
            Title = Titles[Index]
        else:
            Title = None
            
        Plot_Function(Title=Title)
        
    plt.tight_layout()
    plt.show()


