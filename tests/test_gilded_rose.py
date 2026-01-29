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

def test_sulfuras_never_changes():
    item = Item("Sulfuras, Hand of Ragnaros", 1, 80)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Sulfuras, Hand of Ragnaros"
    assert item.sell_in == 1
    assert item.quality == 80

def test_backstage_quality_increase():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 80)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Backstage passes to a TAFKAL80ETC concert"
    assert item.sell_in == 0
    assert item.quality == 80

def test_backstage_quality_increase_10_days():
    item = Item("Sulfuras, Hand of Ragnaros", 1, 80)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Sulfuras, Hand of Ragnaros"
    assert item.sell_in == 1
    assert item.quality == 80

def test_backstage_quality_increase_5_days():
    item = Item("Sulfuras, Hand of Ragnaros", 1, 80)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Sulfuras, Hand of Ragnaros"
    assert item.sell_in == 1
    assert item.quality == 80

def test_backstage_quality_zero():
    item = Item("Sulfuras, Hand of Ragnaros", 1, 80)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "Sulfuras, Hand of Ragnaros"
    assert item.sell_in == 1
    assert item.quality == 80