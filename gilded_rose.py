# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_item()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_item(self):
        """
        - Every item loses **1 Quality** and **1 SellIn** each day.
        - If the sell-by date is **past** (SellIn < 0), **Quality** drops **twice as fast** (–2/day).
        - **Quality never goes below 0**, and never above **50** (some exceptions).
        """
        if self.sell_in < 0:
            self.quality -= 2
        else:
            self.quality -= 1

        if self.quality < 0:
            self.quality = 0

        self.sell_in -= 1

class AgedBrie(Item):
    name = "Aged Brie"
    def update_item(self):
        """
        - Gets better with age: **Quality increases** each day (up to 50).
        - if sellin <0 in aged brie, quality increases in two.
        """
        if self.sell_in < 0:
            self.quality += 2
        else:
            self.quality += 1

        if self.quality > 50:
            self.quality = 50

        self.sell_in -= 1

class Backstage(Item):
    name = "Backstage passes to a TAFKAL80ETC concert"
    def update_item(self):
        """
        - Improve as the concert approaches:
        - +1 Quality per day
        - If 10 days left: **+2 Quality**
        - If 5 days left: **+3 Quality**
        - **After the concert (SellIn < 0): Quality drops to 0**
        """
        if self.sell_in > 5 and self.sell_in <= 10:
            self.quality += 2
        elif self.sell_in >= 0 and self.sell_in <= 5:
            self.quality += 3
        elif self.sell_in < 0:
            self.quality = 0
        else:
            self.quality += 1

        if self.quality > 50:
            self.quality = 50

        self.sell_in -= 1


class Conjured(Item):
    name = "Conjured Item"
    def update_item(self):
        """
        - Spoil faster: **Quality drops twice as fast as normal items**.
        """
        if self.sell_in < 0:
            self.quality -= 4
        else:
            self.quality -= 2

        if self.quality < 0:
            self.quality = 0

        self.sell_in -= 1

class Sulfuras(Item):
    name = "Sulfuras, Hand of Ragnaros"
    def update_item(self):
        """
        - Legendary, never sold!
        - **Quality always 80** and never changes.
        """
        self.sell_in -= 1
        self.quality = 80
