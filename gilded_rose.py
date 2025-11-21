from dataclasses import dataclass

from available_items import SULFURAS, BACKSTAGE_PASS, AGED_BRIE


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == AGED_BRIE:
                aged_brie = AgedBrie(sell_in=item.sell_in, quality=item.quality)
                aged_brie.update_state()
                item.quality = aged_brie.quality
                item.sell_in = aged_brie.sell_in

            elif item.name == BACKSTAGE_PASS:
                backstage_pass = BackstagePass(sell_in=item.sell_in, quality=item.quality)
                backstage_pass.update_state()
                item.quality = backstage_pass.quality
                item.sell_in = backstage_pass.sell_in

            elif item.name == SULFURAS:
                sulfuras = Sulfuras(sell_in=item.sell_in, quality=item.quality)
                sulfuras.update_state()
                item.quality = sulfuras.quality
                item.sell_in = sulfuras.sell_in
            else:
                normal_item = NormalItem(sell_in=item.sell_in, quality=item.quality)
                normal_item.update_state()
                item.quality = normal_item.quality
                item.sell_in = normal_item.sell_in

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


@dataclass
class AgedBrie:
    sell_in: int
    quality: int

    def update_state(self):
        self._update_quality()
        self._update_sell_in()

    def _update_quality(self):
        self.quality += 1
        if self.sell_in <= 0:
            self.quality += 1

        if self.quality > 50:
            self.quality = 50

    def _update_sell_in(self):
        self.sell_in -= 1


@dataclass
class BackstagePass:
    sell_in: int
    quality: int

    def update_state(self):
        self._update_quality()
        self._update_sell_in()

    def _update_quality(self):

        if self.sell_in <= 0:
            self.quality = 0

        elif self.sell_in <= 5:
            self.quality += 3

        elif self.sell_in <= 10:
            self.quality += 2

        else:
            self.quality += 1

        if self.quality > 50:
            self.quality = 50

    def _update_sell_in(self):
        self.sell_in -= 1


@dataclass
class Sulfuras:
    sell_in: int
    quality: int

    def update_state(self):
        self._update_quality()
        self._update_sell_in()

    def _update_quality(self):
        pass

    def _update_sell_in(self):
        pass


@dataclass
class NormalItem:
    sell_in: int
    quality: int

    def update_state(self):
        self._update_quality()
        self._update_sell_in()

    def _update_quality(self):
        self.quality -= 1
        if self.sell_in <= 0:
            self.quality -= 1

        if self.quality < 0:
            self.quality = 0

    def _update_sell_in(self):
        self.sell_in -= 1