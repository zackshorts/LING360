import re

all_count = 0
feature_count = 0

modals = ['can', 'could', 'Should', 'would', 'will']

with open('/Users/zacharyshorts/Downloads/simple.txt', mode="r") as infile:
    cur_file = infile.read()
    print(cur_file)
    print(type(cur_file))
    wds = cur_file.split()
    print(wds)
    print(type(wds))
    wds = re.split(r"[\s\\.\\?!]+", cur_file)
    print(wds)
    print(type(wds))
    wds = [wd for wd in wds if len(wd) > 0]
    print(wds)
    print(len(wds))

    for wd in wds:
        all_count += 1
        if wd in modals:
            feature_count += 1

print(all_count)
print(feature_count)
