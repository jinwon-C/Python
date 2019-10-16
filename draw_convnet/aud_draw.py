import os
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle

NumDots = 4 
NumConvMax = 8 
NumFcMax = 200 

Radius = 0.2

White = 1.
Light = 0.7
Medium = 0.5
Dark = 0.3
Darker = 0.15
Black = 0.

def add_layer(patches, colors, size=(24, 24), num=6,
              top_left=[0, 0],
              loc_diff=[3, -3],
              ):
    # add a rectangle
    top_left = np.array(top_left)
    loc_diff = np.array(loc_diff)
    loc_start = top_left - np.array([0, size[0]])
    for ind in range(num):
        patches.append(Rectangle(loc_start + ind * loc_diff, size[1], size[0]))
        if ind % 2:
            colors.append(Medium)
        else:
            colors.append(Light)


def add_layer_with_omission(patches, colors, size=(0, 0),
                            num=0, num_max=0,
                            num_dots=4,
                            top_left=[0, 0],
                            loc_diff=[3, -3],
                            ):
    # add a rectangle
    top_left = np.array(top_left)
    loc_diff = np.array(loc_diff)
    loc_start = top_left - np.array([0, size[0]])
    this_num = min(num, num_max)
    start_omit = (this_num - num_dots) // 2
    end_omit = this_num - start_omit
    start_omit -= 1
    for ind in range(this_num):
        if (num > num_max) and (start_omit < ind < end_omit):
            omit = True
        else:
            omit = False

        if omit:
            if loc_diff[0] == 0:
                if ind%5 == 2:
                    patches.append(
                        Circle(loc_start + ind * loc_diff + np.append(size[1]/2, size[0]/2), Radius))
            else:
                patches.append(
                #Circle(loc_start + ind * loc_diff + np.array(size) / 2, 0.5))
                #Circle(loc_start + ind * loc_diff - np.append(size[0]/2, 0) , 0.5))
                    Circle(loc_start + ind * loc_diff + np.append(size[1]/2, size[0]/2), Radius))
        else:
            patches.append(Rectangle(loc_start + ind * loc_diff,
                                     size[1], size[0]))

        if omit:
            colors.append(Black)
        elif ind % 2:
            colors.append(Medium)
        else:
            colors.append(Light)
#        if ind > 10:
#            patches.append(Circle(loc_start - ind * np.append(20, 0), 5))


def add_mapping(patches, colors, start_ratio, end_ratio, patch_size, ind_bgn,
                top_left_list, loc_diff_list, num_show_list, size_list):

    start_loc = top_left_list[ind_bgn] \
        + (num_show_list[ind_bgn] - 1) * np.array(loc_diff_list[ind_bgn]) \
        + np.array([start_ratio[0] * (size_list[ind_bgn][1] - patch_size[1]),
                    - start_ratio[1] * (size_list[ind_bgn][0] - patch_size[0])]
                   )

    end_loc = top_left_list[ind_bgn + 1] \
        + (num_show_list[ind_bgn + 1] - 1) * np.array(
            loc_diff_list[ind_bgn + 1]) \
        + np.array([end_ratio[0] * size_list[ind_bgn + 1][1],
                    - end_ratio[1] * size_list[ind_bgn + 1][0]])


    patches.append(Rectangle(start_loc, patch_size[1], -patch_size[0]))
    colors.append(Dark)
    patches.append(Line2D([start_loc[0], end_loc[0]],
                          [start_loc[1], end_loc[1]]))
    colors.append(Darker)
    patches.append(Line2D([start_loc[0] + patch_size[1], end_loc[0]],
                          [start_loc[1], end_loc[1]]))
    colors.append(Darker)
    patches.append(Line2D([start_loc[0], end_loc[0]],
                          [start_loc[1] - patch_size[0], end_loc[1]]))
    colors.append(Darker)
    patches.append(Line2D([start_loc[0] + patch_size[1], end_loc[0]],
                          [start_loc[1] - patch_size[0], end_loc[1]]))
    colors.append(Darker)



def label(xy, text, xy_off=[0, 4]):
    plt.text(xy[0] + xy_off[0], xy[1] + xy_off[1], text,
             family='sans-serif', size=8)


if __name__ == '__main__':

    fc_unit_size = 2
    #layer_width = 40
    layer_width = 80
    flag_omit = True

    patches = []
    colors = []

    fig, ax = plt.subplots()

    ############################
    # conv layers
    #size_list = [(100, 1), (100, 1), (50, 1), (50, 1), (25, 1), (25,1), (13,1), (13, 1), (7, 1), (7, 1), (4, 1), (4, 1), (2, 1)]
    size_list = [(499, 10), (499, 10), (250, 10), (250, 10), (125, 10), (125, 10), (63, 10), (63, 10), (32, 10), (32, 10), (16, 10), (16, 10), (8, 5), (8, 5), (4, 3), (4, 3), (2, 2), (2, 2), (1, 1)]
    num_list = [1, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128, 256, 256, 512, 512, 1024, 1024]
    x_diff_list = [0, layer_width, layer_width, layer_width, layer_width, layer_width, layer_width, layer_width, layer_width, layer_width, layer_width, layer_width, layer_width, layer_width, layer_width, layer_width, layer_width, layer_width, layer_width]
    text_list = ['Inputs'] + ['Feature\nmaps'] * (len(size_list) - 1)
    loc_diff_list = [[3, -3]] * len(size_list)

    num=len(size_list)
    num_max=NumConvMax

    num_show_list = list(map(min, num_list, [NumConvMax] * len(num_list)))
    top_left_list = np.c_[np.cumsum(x_diff_list), np.zeros(len(x_diff_list))]
    circle_position = []
    for ind in range(len(size_list)-1,-1,-1):
        if flag_omit:
            add_layer_with_omission(patches, colors, size=size_list[ind],
                                    num=num_list[ind],
                                    num_max=NumConvMax,
                                    num_dots=NumDots,
                                    top_left=top_left_list[ind],
                                    loc_diff=loc_diff_list[ind])
            circle_position = top_left_list[ind]
        else:
            add_layer(patches, colors, size=size_list[ind],
                      num=num_show_list[ind],
                      top_left=top_left_list[ind], loc_diff=loc_diff_list[ind])
        label(top_left_list[ind], text_list[ind] + '\n{}@{}x{}'.format(
            num_list[ind], size_list[ind][1], size_list[ind][0]))

    ############################
    # in between layers
    start_ratio_list = [[0.4, 0.5], [0.4, 0.8],[0.4, 0.5], [0.4, 0.8],[0.4, 0.5], [0.4, 0.8],[0.4, 0.5], [0.4, 0.8],[0.4, 0.5], [0.4, 0.8],[0.4, 0.5], [0.4, 0.8],[0.4, 0.5], [0.4, 0.8], [0.4, 0.5], [0.4, 0.8], [0.4, 0.5], [0.4, 0.8]]
    end_ratio_list = [[0.4, 0.5], [0.4, 0.8],[0.4, 0.5], [0.4, 0.8],[0.4, 0.5], [0.4, 0.8],[0.4, 0.5], [0.4, 0.8],[0.4, 0.5], [0.4, 0.8],[0.4, 0.5], [0.4, 0.8],[0.4, 0.5], [0.4, 0.8], [0.4, 0.5], [0.4, 0.8], [0.4, 0.5], [0.4, 0.8]]
    patch_size_list = [(3, 1), (2, 1),(3, 1), (2, 1),(3, 1), (2, 1),(3, 1), (2, 1),(3, 1), (2, 1),(3, 1), (2, 1), (3, 1), (2, 1), (3, 1), (2, 1), (3, 1), (2, 1)]
    ind_bgn_list = range(len(patch_size_list))
    text_list = ['conv', 'pool','conv', 'pool','conv', 'pool','conv', 'pool','conv', 'pool','conv', 'pool','conv', 'pool', 'conv', 'pool', 'conv','pool']

    for ind in range(len(patch_size_list)):
        add_mapping(
            patches, colors, start_ratio_list[ind], end_ratio_list[ind],
            patch_size_list[ind], ind,
            top_left_list, loc_diff_list, num_show_list, size_list)
        x_off = 55
        y_off = -50
        if ind == 0:
            x_off = 30
            y_off = -80
        elif ind == 1:
            x_off = 40
            y_off = -100
        elif ind == 2:
            x_off = 30
        label(top_left_list[ind], text_list[ind] + '\n{}x{}'.format(
            patch_size_list[ind][1], patch_size_list[ind][0]), xy_off=[x_off, y_off]
        )

    ############################
    # fully connected layers
    size_list = [(fc_unit_size, fc_unit_size)] * 2
    num_list = [1024, 10]
    num_show_list = list(map(min, num_list, [NumFcMax] * len(num_list)))
    x_diff_list = [sum(x_diff_list) + layer_width, layer_width, layer_width]
    top_left_list = np.c_[np.cumsum(x_diff_list), np.zeros(len(x_diff_list))]
    #loc_diff_list = [[fc_unit_size, -fc_unit_size]] * len(top_left_list)
    loc_diff_list = [[0, -fc_unit_size]] * len(top_left_list)
    text_list = ['Hidden\nunits'] * (len(size_list) - 1) + ['Outputs']

    for ind in range(len(size_list)):
        if flag_omit:
            add_layer_with_omission(patches, colors, size=size_list[ind],
                                    num=num_list[ind],
                                    num_max=NumFcMax,
                                    num_dots=100,
                                    top_left=top_left_list[ind],
                                    loc_diff=loc_diff_list[ind])
        else:
            add_layer(patches, colors, size=size_list[ind],
                      num=num_show_list[ind],
                      top_left=top_left_list[ind],
                      loc_diff=loc_diff_list[ind])
        label(top_left_list[ind], text_list[ind] + '\n{}'.format(
            num_list[ind]))

    text_list = ['Flatten\n', 'Fully\nconnected']

    for ind in range(len(size_list)):
        label(top_left_list[ind], text_list[ind], xy_off=[-50, -65])

    ############################
    for patch, color in zip(patches, colors):
        patch.set_color(color * np.ones(3))
        if isinstance(patch, Line2D):
            ax.add_line(patch)
        else:
            patch.set_edgecolor(Black * np.ones(3))
            ax.add_patch(patch)

    plt.tight_layout()
    plt.axis('equal')
    plt.axis('off')
    #plt.show()
    #fig.set_size_inches(8, 2.5)
    fig.set_size_inches(32, 16)


    fig_dir = './'
    fig_ext = '.png'
    fig.savefig(os.path.join(fig_dir, 'aud_arch' + fig_ext),
                bbox_inches='tight', pad_inches=0)
