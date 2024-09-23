import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#######################################################################################################################
# CREATE #
#######################################################################################################################

import matplotlib.pyplot as plt
import seaborn as sns

# See documentation in "Graphio - Plot Functions.txt" for parameter options.

def Create_Line_Plot(X, Y, Title = None, X_Label = 'X', Y_Label = 'Y', Colors = None, Grid = True, Figure_Size = (10, 6), 
                     Font_Size = 12, Alpha = 1.0, X_Lim = None, Y_Lim = None, X_Scale = 'linear', Y_Scale = 'linear',
                     Label = None, Legend = False, Legend_Location = 'best', Legend_Font_Size = 12, 
                     Marker_Style = 'o', Line_Style = '-', Line_Width = 2, Horizontal_Lines = None, Vertical_Lines = None, 
                     Annotations = None, File_Name = None, File_Format = 'png', X_Label_Rotation = 0):
    
    plt.figure(figsize = Figure_Size)
    
    if Colors:
        plt.plot(X, Y, color = Colors[0], marker = Marker_Style, linestyle = Line_Style, linewidth = Line_Width, alpha = Alpha, label = Label)
    else:
        plt.plot(X, Y, marker = Marker_Style, linestyle = Line_Style, linewidth = Line_Width, alpha = Alpha, label = Label)
    
    plt.xscale(X_Scale)
    plt.yscale(Y_Scale)
    
    if X_Lim:
        plt.xlim(X_Lim)
    if Y_Lim:
        plt.ylim(Y_Lim)
    
    if Title:
        plt.title(Title, fontsize = Font_Size)
    plt.xlabel(X_Label, fontsize = Font_Size)
    plt.ylabel(Y_Label, fontsize = Font_Size)
    
    plt.xticks(rotation = X_Label_Rotation)
    
    if Grid:
        plt.grid(True)
    
    if Horizontal_Lines:
        for line in Horizontal_Lines:
            plt.axhline(y = line, color = 'gray', linestyle = '--')
    if Vertical_Lines:
        for line in Vertical_Lines:
            plt.axvline(x = line, color = 'gray', linestyle = '--')
    
    if Annotations:
        for annotation in Annotations:
            plt.annotate(annotation['text'], xy = annotation['xy'], xytext = annotation['xytext'], 
                         arrowprops = annotation.get('arrowprops', {}))
    
    if Legend and Label:
        plt.legend(loc = Legend_Location, fontsize = Legend_Font_Size)
    
    if File_Name:
        plt.savefig(f'{File_Name}.{File_Format}', format = File_Format, bbox_inches = 'tight')
    
    plt.show()

def Create_Histogram(Data, Title = None, X_Label = 'X', Y_Label = 'Y', Bins = 10, Colors = None, Alpha = 0.7, 
                     Grid = True, Figure_Size = (10, 6), Font_Size = 12, X_Lim = None, Y_Lim = None, 
                     Legend = False, Legend_Location = 'best', Legend_Font_Size = 12, 
                     Horizontal_Lines = None, Vertical_Lines = None, Annotations = None, File_Name = None, File_Format = 'png'):
    
    plt.figure(figsize = Figure_Size)
    
    if Colors:
        plt.hist(Data, bins = Bins, color = Colors[0], alpha = Alpha, label = X_Label)
    else:
        plt.hist(Data, bins = Bins, alpha = Alpha, label = X_Label)
    
    if X_Lim:
        plt.xlim(X_Lim)
    if Y_Lim:
        plt.ylim(Y_Lim)
    
    if Title:
        plt.title(Title, fontsize = Font_Size)
    plt.xlabel(X_Label, fontsize = Font_Size)
    plt.ylabel(Y_Label, fontsize = Font_Size)
    
    if Grid:
        plt.grid(True)
    
    if Horizontal_Lines:
        for line in Horizontal_Lines:
            plt.axhline(y = line, color = 'gray', linestyle = '--')
    if Vertical_Lines:
        for line in Vertical_Lines:
            plt.axvline(x = line, color = 'gray', linestyle = '--')
    
    if Annotations:
        for annotation in Annotations:
            plt.annotate(annotation['text'], xy = annotation['xy'], xytext = annotation['xytext'], 
                         arrowprops = annotation.get('arrowprops', {}))
    
    if Legend:
        plt.legend(loc = Legend_Location, fontsize = Legend_Font_Size)
    
    if File_Name:
        plt.savefig(f'{File_Name}.{File_Format}', format = File_Format, bbox_inches = 'tight')
    
    plt.show()

def Create_Bar_Plot(Categories, Values, Title = None, X_Label = 'X', Y_Label = 'Y', Colors = None, Grid = True, Figure_Size = (10, 6), 
                    Font_Size = 12, Orientation = 'vertical', X_Lim = None, Y_Lim = None, Legend = False, 
                    Legend_Location = 'best', Legend_Font_Size = 12, File_Name = None, File_Format = 'png'):
    
    plt.figure(figsize = Figure_Size)
    
    if Colors:
        if Orientation == 'horizontal':
            plt.barh(Categories, Values, color = Colors)
        else:
            plt.bar(Categories, Values, color = Colors)
    else:
        if Orientation == 'horizontal':
            plt.barh(Categories, Values)
        else:
            plt.bar(Categories, Values)
    
    if X_Lim:
        plt.xlim(X_Lim)
    if Y_Lim:
        plt.ylim(Y_Lim)
    
    if Title:
        plt.title(Title, fontsize = Font_Size)
    plt.xlabel(X_Label, fontsize = Font_Size)
    plt.ylabel(Y_Label, fontsize = Font_Size)
    
    if Grid:
        plt.grid(axis = 'y')
    
    if Legend:
        plt.legend(loc = Legend_Location, fontsize = Legend_Font_Size)
    
    if File_Name:
        plt.savefig(f'{File_Name}.{File_Format}', format = File_Format, bbox_inches = 'tight')
    
    plt.show()

def Create_Box_Plot(Data, Title = None, X_Label = 'X', Y_Label = 'Y', Grid = True, Figure_Size = (10, 6), 
                    Font_Size = 12, X_Lim = None, Y_Lim = None, Legend = False, Legend_Location = 'best', 
                    Legend_Font_Size = 12, File_Name = None, File_Format = 'png'):
    
    plt.figure(figsize = Figure_Size)
    sns.boxplot(data = Data)
    
    if X_Lim:
        plt.xlim(X_Lim)
    if Y_Lim:
        plt.ylim(Y_Lim)
    
    if Title:
        plt.title(Title, fontsize = Font_Size)
    plt.xlabel(X_Label, fontsize = Font_Size)
    plt.ylabel(Y_Label, fontsize = Font_Size)
    
    if Grid:
        plt.grid(True)
    
    if Legend:
        plt.legend(loc = Legend_Location, fontsize = Legend_Font_Size)
    
    if File_Name:
        plt.savefig(f'{File_Name}.{File_Format}', format = File_Format, bbox_inches = 'tight')
    
    plt.show()

def Create_Scatter_Plot_With_Regression(X, Y, Title = None, X_Label = 'X', Y_Label = 'Y', Colors = None, Grid = True, 
                                         Figure_Size = (10, 6), Font_Size = 12, Alpha = 1.0, X_Lim = None, Y_Lim = None, 
                                         X_Scale = 'linear', Y_Scale = 'linear', Legend = False, Legend_Location = 'best', 
                                         Legend_Font_Size = 12, Horizontal_Lines = None, Vertical_Lines = None, 
                                         Annotations = None, File_Name = None, File_Format = 'png'):
    
    plt.figure(figsize = Figure_Size)
    
    if Colors:
        sns.regplot(x = X, y = Y, scatter_kws = {'color': Colors[0], 'alpha': Alpha}, line_kws = {'color': 'red'})
    else:
        sns.regplot(x = X, y = Y, scatter_kws = {'alpha': Alpha}, line_kws = {'color': 'red'})
    
    plt.xscale(X_Scale)
    plt.yscale(Y_Scale)
    
    if X_Lim:
        plt.xlim(X_Lim)
    if Y_Lim:
        plt.ylim(Y_Lim)
    
    if Title:
        plt.title(Title, fontsize = Font_Size)
    plt.xlabel(X_Label, fontsize = Font_Size)
    plt.ylabel(Y_Label, fontsize = Font_Size)
    
    if Grid:
        plt.grid(True)
    
    if Horizontal_Lines:
        for line in Horizontal_Lines:
            plt.axhline(y = line, color = 'gray', linestyle = '--')
    if Vertical_Lines:
        for line in Vertical_Lines:
            plt.axvline(x = line, color = 'gray', linestyle = '--')
    
    if Annotations:
        for annotation in Annotations:
            plt.annotate(annotation['text'], xy = annotation['xy'], xytext = annotation['xytext'], 
                         arrowprops = annotation.get('arrowprops', {}))
    
    if Legend:
        plt.legend(loc = Legend_Location, fontsize = Legend_Font_Size)
    
    if File_Name:
        plt.savefig(f'{File_Name}.{File_Format}', format = File_Format, bbox_inches = 'tight')
    
    plt.show()

def Create_Violin_Plot(Data, Title = None, X_Label = 'X', Y_Label = 'Y', Grid = True, Figure_Size = (10, 6), 
                       Font_Size = 12, X_Lim = None, Y_Lim = None, Label = None, Legend = False):
    
    plt.figure(figsize=Figure_Size)
    sns.violinplot(data=Data)
    
    if X_Lim:
        plt.xlim(X_Lim)
    if Y_Lim:
        plt.ylim(Y_Lim)
    
    if Title:
        plt.title(Title, fontsize=Font_Size)
    plt.xlabel(X_Label, fontsize=Font_Size)
    plt.ylabel(Y_Label, fontsize=Font_Size)
    
    if Grid:
        plt.grid(True)
    
    if Legend and Label:
        plt.legend()
    
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

#######################################################################################################################
# CORRELATIONS #
#######################################################################################################################

def Correlation_Heatmap(df: pd.DataFrame, 
                                    Title = None, 
                                    X_Label = None,
                                    Y_Label = None,
                                    File = None):
    
    """
    Creates a half-masked heatmap of the correlation matrix from the input DataFrame.
    Only the lower triangular part of the heatmap is shown, while the upper part is masked.

    Example:
    Half_Masked_Correlation_Heatmap(df, Title="Correlation Heatmap", File="heatmap.png")

    """

    plt.figure(figsize = (9,9))
    sns.set(font_scale = 1)

    # Mask of zeros with the same size of the matrix of correlation.
    Mask = np.zeros_like(df.corr())

    # Hide a half part of the matrix.
    Mask[np.triu_indices_from(Mask)] = True

    with sns.axes_style('white'):
        sns.heatmap(df.corr(), mask = Mask, annot = True, cmap = 'coolwarm')
    
    if Title:
        plt.title(Title)
        plt.xlabel(X_Label)
        plt.ylabel(Y_Label)

    if File:
        plt.savefig(File, bbox_inches = 'tight')
    
    plt.show()

    return
