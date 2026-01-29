from gilded_rose import GildedRose, Item


def test_foo():
    item = Item("foo", 1, 1)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "foo"
    assert item.sell_in == 0
    assert item.quality == 0

def test_aged_brie():
    item = Item("Aged Brie", 10, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Aged Brie"
    assert item.sell_in == 9
    assert item.quality == 1

def test_sulfuras():
    item = Item("Sulfuras, Hand of Ragnaros", 1, 80)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Sulfuras, Hand of Ragnaros"
    assert item.sell_in == 1
    assert item.quality == 80