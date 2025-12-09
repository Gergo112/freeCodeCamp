# 1)
from mean_var_std import calculate

print(calculate([0,1,2,3,4,5,6,7,8]))

# 2)
from demographic_data_analyzer import calculate_demographic_data

if __name__ == "__main__":
    calculate_demographic_data()

# 3)
from medical_data_visualizer import draw_cat_plot, draw_heat_map

draw_cat_plot()
draw_heat_map()

# 4)
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

draw_line_plot()
draw_bar_plot()
draw_box_plot()

#5)
from sea_level_predictor import draw_plot

draw_plot()