from gilded_rose import Item, GildedRose

if __name__ == "__main__":
    items = [
             Item(name="Dummy Item", sell_in=10, quality=20),
             Item(name="Another dummy Item", sell_in=5, quality=1),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=18, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=7, quality=30),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=15),
            ]

    days = 3
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()