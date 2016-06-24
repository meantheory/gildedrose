# -*- coding: utf-8 -*-
# import unittest
import pytest
from rose2 import Item
from rose2 import GildedRose

tstdata = [
    (Item(name="+5 Dexterity Vest", sell_in=10, quality=20), [
        [9, 19],
        [8, 18],
        [7, 17],
        [6, 16],
        [5, 15]
    ]),
    (Item(name="Aged Brie", sell_in=2, quality=0), [
        [1, 1],
        [0, 2],
        [-1, 4],
        [-2, 6],
        [-3, 8],
    ]),
    (Item(name="Elixir of the Mongoose", sell_in=5, quality=7), [
        [4, 6],
        [3, 5],
        [2, 4],
        [1, 3],
        [0, 2],
    ]),
    (Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80), [
        [0, 80],
        [0, 80],
        [0, 80],
        [0, 80],
        [0, 80],
    ]),
    (Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80), [
        [-1, 80],
        [-1, 80],
        [-1, 80],
        [-1, 80],
        [-1, 80],
    ]),
    (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20), [
        [14, 21],
        [13, 22],
        [12, 23],
        [11, 24],
        [10, 25],
    ]),
    (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49), [
        [9, 50],
        [8, 50],
        [7, 50],
        [6, 50],
        [5, 50],
    ]),
    (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49), [
        [4, 50],
        [3, 50],
        [2, 50],
        [1, 50],
        [0, 50],
    ]),
    (Item(name="Conjured Mana Cake", sell_in=3, quality=6), [
        [2, 5],
        [1, 4],
        [0, 3],
        [-1, 1],
        [-2, 0],
    ]),
]

@pytest.mark.parametrize("item,tstexpect", tstdata, scope="function")
def test_modified(item, tstexpect):
    gr = GildedRose(list([item]))
    print(gr.items)

    for expected in tstexpect:
        gr.update_quality()
        ref = gr.items[0]
        print(expected, ref.sell_in, ref.quality)
        assert expected == [ref.sell_in, ref.quality]

# if __name__ == '__main__':
#     unittest.main()
