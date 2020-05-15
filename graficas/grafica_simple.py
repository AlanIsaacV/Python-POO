from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure(title='Bubble sort',
                    x_axis_label='Tamaño de lista', y_axis_label='Pasos')
    x_vals = [x for x in range(20)]
    y_vals = [0,1,2, 3, 9, 14, 20, 27, 35, 44, 54,
                65, 77, 90, 104, 119, 135, 152, 170, 189]
    fig.line(x_vals, y_vals, legend_label='(n^2)/2 - xn', line_width=2)
    show(fig)