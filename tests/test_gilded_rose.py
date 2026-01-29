from gilded_rose import GildedRose, Item


def test_general_item_reduces_quality_every_day():
    item = Item("foo", 10, 10)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 9
    assert item.quality == 9

def test_general_item_never_goes_below_zero():
    item = Item("foo", 0, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == -1
    assert item.quality == 0

def test_sulfuras_quality_always_80():
    item = Item("Sulfuras, Hand of Ragnaros", 0, 80)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 0
    assert item.quality == 80

def test_general_decrements_two_over_sell_in_below_zero():
    item = Item("foo", -1, 30)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == -2
    assert item.quality == 28

def test_quality_goes_to_zero_after_concert():
    item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 30)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == -2
    assert item.quality == 0



def test_backstage_15_sell_in_increase_quality_1():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 15, 40)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 14
    assert item.quality == 41

def test_backstage_10_sell_in_increase_quality_2():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 40)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 9
    assert item.quality == 42

def test_backstage_5_sell_in_increase_quality_3():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 40)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 43

def test_aged_brie_never_goes_above_50():
    item = Item("Aged Brie", 5, 50)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 50

def test_aged_brie_increase_quality():
    item = Item("Aged Brie", 5, 40)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 41

def test_aged_brie_double_increase_quality_bellow_sell_in_zerp():
    item = Item("Aged Brie", -1, 30)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == -2
    assert item.quality == 32