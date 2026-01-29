# -*- coding: utf-8 -*-
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONCERT_TICKETS = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == SULFURAS:
                item.quality = 80
            elif item.name == AGED_BRIE:
                if item.sell_in < 0:
                    item.quality += 2
                elif item.quality < 50:
                    item.quality +=1
                item.sell_in -=1
            elif item.name == CONCERT_TICKETS:
                if item.sell_in < 0:
                    item.quality = 0
                elif item.sell_in <= 5:
                    item.quality += 3
                elif item.sell_in <= 10:
                    item.quality += 2
                else:
                    item.quality += 1
                item.sell_in -=1
            else:
                if item.sell_in < 0:
                    item.quality -= 2
                    item.sell_in -= 1
                else:
                    item.sell_in -= 1
                    item.quality -= 1
                if item.quality < 0:
                    item.quality =0
                elif item.quality > 50:
                    item.quality =50

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
