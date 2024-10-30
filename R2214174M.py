import matplotlib.pyplot as plt

def plot_data():

    txt_file = open('C:/Downloads/x_y_coordinates.txt', 'r')

    x_coords = []
    y_coords = []
    txt_file.readline()

    for line in txt_file.readlines():
        x_coords.append(float(line.split(',')[0]))
        y_coords.append(float(line.split(',')[1]))

    plt.scatter(x_coords, y_coords)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()
plot_data()