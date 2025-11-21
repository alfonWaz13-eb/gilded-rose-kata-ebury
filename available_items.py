from dataclasses import dataclass

SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"
NORMAL_ITEM = "foo"


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
