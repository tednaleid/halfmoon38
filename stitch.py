# modified from: https://gist.github.com/glombard/7cd166e311992a828675

# Combine multiple images into one.
#
# To install the Pillow module on Mac OS X:
#
# $ xcode-select --install
# $ brew install libtiff libjpeg webp little-cms2
# $ pip install Pillow
#

from __future__ import print_function
import os

from PIL import Image

result = Image.new("LA", (3584, 4605))

# all images are 256x256 except for the last row which is only 253 wide
for x_index in range(18):
    for y_index in range(14):
        file = './raw/{0}_{1}.jpg'.format(y_index, x_index)
        width = 256 if x_index < 17 else 253
        height = 256
        print('{0} {1}x{2}'.format(file, width, height))

        path = os.path.expanduser(file)
        img = Image.open(path)
        img.thumbnail((width, height), Image.ANTIALIAS)
        x = x_index * 256
        y = y_index * 256
        print('pos {0},{1} size {2},{3}'.format(x, y, width, height))
        result.paste(img, (x, y, x + width, y + height))
        converted_result = result.convert('RGB')
        converted_result.save(os.path.expanduser('./output.jpg'))
