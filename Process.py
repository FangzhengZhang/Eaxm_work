import math
import matplotlib.pyplot as plt

city_list = {}


def read_bench( file_name):
    with open(file_name) as fp:
        line = fp.readline()
        while line:
            city_info = line.split()
            city_list[city_info[0]] = (city_info[1],city_info[2])
            line = fp.readline()


def read_bench_limited( file_name):
    n=0
    with open(file_name) as fp:
        line = fp.readline()
        while n < 10:
            city_info = line.split()
            city_list[city_info[0]] = (city_info[1],city_info[2])
            line = fp.readline()
            n+=1


def get_distance(p1, p2):
    return math.sqrt(((p1.city_x - p2.city_x) ** 2) + ((p1.city_y - p2.city_y) ** 2))


def plot_dot_chart(cl):
    xs = []
    ys = []
    for key in cl:
        xs.append(cl[key][0])
        ys.append(cl[key][1])
    plt.plot(xs,ys, 'ro')
    plt.show()


def brute_force():
    """Check all the edges, and find the optimal one"""
    checked_list=[]
    marked_path = []
    cost = -1
    for city in city_list:



read_bench_limited("bench1.txt")
#read_bench("bench1.txt")
#print(city_list)
plot_dot_chart(city_list)