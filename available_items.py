from abc import ABC, abstractmethod

SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"
NORMAL_ITEM = "foo"


class GildedRoseProduct(ABC):

    def __init__(self, sell_in, quality):
        self.sell_in = sell_in
        self.quality = quality

    def update_state(self):
        self._update_quality()
        self._update_sell_in()

    @abstractmethod
    def _update_quality(self): ...

    @abstractmethod
    def _update_sell_in(self): ...


class AgedBrie(GildedRoseProduct):

    def _update_quality(self):
        self.quality += 1
        if self.sell_in <= 0:
            self.quality += 1

        if self.quality > 50:
            self.quality = 50

    def _update_sell_in(self):
        self.sell_in -= 1


class BackstagePass(GildedRoseProduct):

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


class Sulfuras(GildedRoseProduct):

    def _update_quality(self):
        pass

    def _update_sell_in(self):
        pass


class NormalItem(GildedRoseProduct):

    def _update_quality(self):
        self.quality -= 1
        if self.sell_in <= 0:
            self.quality -= 1

        if self.quality < 0:
            self.quality = 0

    def _update_sell_in(self):
        self.sell_in -= 1
