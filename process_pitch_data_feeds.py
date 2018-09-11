#!/usr/bin/env python
__author__ = 'Tony Moozhayil'
from collections import Counter


def handle():
    try:
        with open('/Users/tonycmooz/Downloads/pitch_example_data', 'r') as f:
            cnt = Counter()
            for i, row in enumerate(f):
                row = row.lstrip('S')
                timestamp, message_type, order_id, indicator, shares, symbol, price, display = \
                    row[:8], row[8:9], row[9:21], row[21:22], row[22:28], row[28:34], row[34:44], row[44:45]
                print timestamp, message_type, order_id, indicator, shares, symbol, price, display
                # if message_type is not ('B', 's', 'r', 'd', 'H', 'I', 'J', 'R'):
                #     cnt[symbol] += 1
    except ValueError:
        print 'Something went wrong!'

    # return cnt.most_common(11)[1:]


if __name__ == "__main__":
    handle()
