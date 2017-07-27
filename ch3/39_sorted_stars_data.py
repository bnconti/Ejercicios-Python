# Exercise 3.39: Write a sort function for a list of 4-tuples
# Author: Bruno N. Conti
# Date: 7/27/17
# Run pytest 39_sorted_stars_data.py for testing

"""
SAMPLE RUN:
╒═════════════════════╤══════════════════════════════════════╤═══════════════════════╤══════════════╕
│ Name of the star    │   Distance to the sun in light years │   Apparent brightness │   Luminosity │
╞═════════════════════╪══════════════════════════════════════╪═══════════════════════╪══════════════╡
│ Alpha Centauri C    │                                  4.2 │                1e-05  │       6e-05  │
├─────────────────────┼──────────────────────────────────────┼───────────────────────┼──────────────┤
│ Alpha Centauri A    │                                  4.3 │                0.26   │       1.56   │
├─────────────────────┼──────────────────────────────────────┼───────────────────────┼──────────────┤
│ Alpha Centauri B    │                                  4.3 │                0.077  │       0.45   │
├─────────────────────┼──────────────────────────────────────┼───────────────────────┼──────────────┤
│ Barnard's Star      │                                  6   │                4e-05  │       0.0005 │
├─────────────────────┼──────────────────────────────────────┼───────────────────────┼──────────────┤
│ Wolf 359            │                                  7.7 │                1e-06  │       2e-05  │
├─────────────────────┼──────────────────────────────────────┼───────────────────────┼──────────────┤
│ BD +36 degrees 2147 │                                  8.2 │                0.0003 │       0.006  │
├─────────────────────┼──────────────────────────────────────┼───────────────────────┼──────────────┤
│ Luyten 726-8 A      │                                  8.4 │                3e-06  │       6e-05  │
├─────────────────────┼──────────────────────────────────────┼───────────────────────┼──────────────┤
│ Luyten 726-8 B      │                                  8.4 │                2e-06  │       4e-05  │
├─────────────────────┼──────────────────────────────────────┼───────────────────────┼──────────────┤
│ Sirius A            │                                  8.6 │                1      │      23.6    │
├─────────────────────┼──────────────────────────────────────┼───────────────────────┼──────────────┤
│ Sirius B            │                                  8.6 │                0.001  │       0.003  │
├─────────────────────┼──────────────────────────────────────┼───────────────────────┼──────────────┤
│ Ross 154            │                                  9.4 │                2e-05  │       0.0005 │
╘═════════════════════╧══════════════════════════════════════╧═══════════════════════╧══════════════╛
DATA SORTED BY 'Distance to the sun in light years'.
"""

from operator import itemgetter
from tabulate import tabulate

data = [
('Alpha Centauri A',    4.3,  0.26,      1.56),
('Alpha Centauri B',    4.3,  0.077,     0.45),
('Alpha Centauri C',    4.2,  0.00001,   0.00006),
("Barnard's Star",      6.0,  0.00004,   0.0005),
('Wolf 359',            7.7,  0.000001,  0.00002),
('BD +36 degrees 2147', 8.2,  0.0003,    0.006),
('Luyten 726-8 A',      8.4,  0.000003,  0.00006),
('Luyten 726-8 B',      8.4,  0.000002,  0.00004),
('Sirius A',            8.6,  1.00,      23.6),
('Sirius B',            8.6,  0.001,     0.003),
('Ross 154',            9.4,  0.00002,   0.0005),
]


def sort(data, item):
    """
    item 1: distance to the sun in light years
    item 2: apparent brightness
    item 3: luminosity
    """
    assert 1 <= item <= 3, "Out of range"
    titles = {0: "Name of the star", 1: "Distance to the sun in light years", 2: "Apparent brightness", 3: "Luminosity"}
    data.sort(key=itemgetter(item))
    print(tabulate(data, tablefmt="fancy_grid",
                   headers=["Name of the star", "Distance to the sun in light years", "Apparent brightness", "Luminosity"]))
    print("DATA SORTED BY '{}'.".format(titles.get(item)))
sort(data, 1)
