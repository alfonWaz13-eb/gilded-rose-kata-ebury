from gilded_rose import GildedRose, Item

# general rules tests
def test_quality_sellin_ok():
    item = Item("foo", 1, 1)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "foo"
    assert item.sell_in == 0
    assert item.quality == 0

def test_quality_sellin_expired():
    item = Item("foo", 0, 2)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "foo"
    assert item.sell_in == -1
    assert item.quality == 0

def test_quality_min():
    item = Item("foo", 1, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "foo"
    assert item.sell_in == 0
    assert item.quality == 0

def test_quality_max():
    item = Item("Aged Brie", 1, 50)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Aged Brie"
    assert item.sell_in == 0
    assert item.quality == 50

# special items tests
def test_aged_brie_quality_increase():
    item = Item("Aged Brie", 10, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Aged Brie"
    assert item.sell_in == 9
    assert item.quality == 1

def test_aged_brie_never_expires():
    item = Item("Aged Brie", -1, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Aged Brie"
    assert item.sell_in == -2
    # it increases the quality twice when expired
    assert item.quality == 2

def test_sulfuras_never_changes():
    item = Item("Sulfuras, Hand of Ragnaros", 1, 80)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Sulfuras, Hand of Ragnaros"
    assert item.sell_in == 1
    assert item.quality == 80

def test_backstage_quality_increase():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 11, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Backstage passes to a TAFKAL80ETC concert"
    assert item.sell_in == 10
    assert item.quality == 1

def test_backstage_quality_increase_10_days():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Backstage passes to a TAFKAL80ETC concert"
    assert item.sell_in == 9
    assert item.quality == 2

def test_backstage_quality_increase_5_days():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Backstage passes to a TAFKAL80ETC concert"
    assert item.sell_in == 4
    assert item.quality == 3

def test_backstage_quality_max():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 50)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Backstage passes to a TAFKAL80ETC concert"
    assert item.sell_in == 4
    assert item.quality == 50


def test_backstage_quality_zero():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Backstage passes to a TAFKAL80ETC concert"
    assert item.sell_in == -1
    assert item.quality == 0

def test_conjured_item_quality_drop():
    item = Item("Conjured Item", 1, 2)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Conjured Item"
    assert item.sell_in == 0
    assert item.quality == 0

def test_conjured_item_quality_drop_expired():
    item = Item("Conjured Item", -1, 4)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Conjured Item"
    assert item.sell_in == -2
    assert item.quality == 0

def test_conjured_item_quality_drop_zero():
    item = Item("Conjured Item", -1, 2)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Conjured Item"
    assert item.sell_in == -2
    assert item.quality == 0

def test_print_item():
    item = Item("foo", 5, 10)
    assert repr(item) == "foo, 5, 10"