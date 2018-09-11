#!/usr/bin/env python
<<<<<<< HEAD
__author__ = 'Tony Moozhayil'
=======
__author__ = 'tonycmooz'
>>>>>>> 8b6498ad39bea4b09d33111768150f7d9e863d06
from collections import Counter


def handle():
<<<<<<< HEAD
    try:
        with open('/Users/tonycmooz/Downloads/pitch_example_data', 'r') as f:
            cnt = Counter()
            for i, row in enumerate(f):
=======
    with open('/Users/tonycmooz/Downloads/pitch_example_data', 'r') as f:
        cnt = Counter()
        for i, row in enumerate(f):
            try:
>>>>>>> 8b6498ad39bea4b09d33111768150f7d9e863d06
                row = row.lstrip('S')
                timestamp, message_type, order_id, indicator, shares, symbol, price, display = \
                    row[:8], row[8:9], row[9:21], row[21:22], row[22:28], row[28:34], row[34:44], row[44:45]
                print timestamp, message_type, order_id, indicator, shares, symbol, price, display
                # if message_type is not ('B', 's', 'r', 'd', 'H', 'I', 'J', 'R'):
                #     cnt[symbol] += 1
<<<<<<< HEAD
    except ValueError:
        print 'Something went wrong!'
=======
            except ValueError:
                print 'Failed: {}'.format(i)
>>>>>>> 8b6498ad39bea4b09d33111768150f7d9e863d06

    # return cnt.most_common(11)[1:]


if __name__ == "__main__":
    handle()
