# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                updater = AgedBrieUpdater()
                updater.update_quality(item)
                return

            if item.name == "Sulfuras, Hand of Ragnaros":
                updater = SulfurasUpdater()
                updater.update_quality(item)
                return

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                updater = BackstagePassesUpdater()
                updater.update_quality(item)
                return

            updater = Updater()
            updater.update_quality(item)
            


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Updater:
    def update_quality(self, item):
        item.sell_in = item.sell_in - 1
        item.quality = item.quality - 1
        if item.sell_in < 0:
            item.quality = item.quality - 1
        if item.quality < 0:
            item.quality = 0

class AgedBrieUpdater(Updater):
    def update_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
        if item.sell_in <= 0 and item.quality < 50:
            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1

class SulfurasUpdater(Updater):
    def update_quality(self, item):
        return
    
class BackstagePassesUpdater(Updater):
    def update_quality(self, item):
        if item.sell_in > 10:
                item.quality = item.quality + 1
        elif item.sell_in > 5:
                item.quality = item.quality + 2
        elif item.sell_in > 0:
                item.quality = item.quality + 3
        else:
            item.quality = 0
        if item.quality > 50:
            item.quality = 50
        item.sell_in = item.sell_in - 1