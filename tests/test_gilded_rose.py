from gilded_rose import GildedRose, Item


def test_foo():
    item = Item("foo", 0, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "foo"


def test_repr_item():
    item = Item("item_test", 10, 20)
    assert item
    assert item.name == "item_test"
    assert repr(item) == "item_test, 10, 20"


def test_item_dummy():
    item = Item("Dummy Item", 10, 20)
    gilded_rose = GildedRose(items=[item])
    gilded_rose.update_quality()
    assert item.name == "Dummy Item"
    assert item.sell_in == 9
    assert item.quality == 19

def test_item_another_dummy():
    item = Item(name="Another dummy Item", sell_in=-1, quality=3)
    gilded_rose = GildedRose(items=[item])
    gilded_rose.update_quality()
    assert item.name == "Another dummy Item"
    assert item.sell_in == -2
    assert item.quality == 1


def test_item_backstage_TAFKAL80ETC():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=20)
    gilded_rose = GildedRose(items=[item])
    gilded_rose.update_quality()
    assert item.name == "Backstage passes to a TAFKAL80ETC concert"
    assert item.sell_in == 2
    assert item.quality == 23

def test_item_backstage_TAFKAL80ETC_sellin_passed_quality_zero():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=10)
    gilded_rose = GildedRose(items=[item])
    gilded_rose.update_quality()
    assert item.name == "Backstage passes to a TAFKAL80ETC concert"
    assert item.sell_in == -2
    assert item.quality == 0

def test_item_Aged_Brie():
    item = Item(name="Aged Brie", sell_in=-1, quality=2)
    gilded_rose = GildedRose(items=[item])
    gilded_rose.update_quality()
    assert item.name == "Aged Brie"
    assert item.sell_in == -2
    assert item.quality == 4

def test_item_sulfuras():
    item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)
    gilded_rose = GildedRose(items=[item])
    gilded_rose.update_quality()
    assert item.name == "Sulfuras, Hand of Ragnaros"
    assert item.sell_in == -1
    assert item.quality == 80