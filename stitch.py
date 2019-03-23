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
for i in range(14):
    for j in range(18):
        file = './raw/{0}_{1}.jpg'.format(i, j)
        width = 256 if j < 17 else 253
        height = 256
        print('{0} {1}x{2}'.format(file, width, height))

        path = os.path.expanduser(file)
        img = Image.open(path)
        img.thumbnail((width, height), Image.ANTIALIAS)
        x = i * 256
        y = j * 256
        print('pos {0},{1} size {2},{3}'.format(x, y, width, height))
        result.paste(img,  (x, y, x + width, y + height))
        converted_result = result.convert('RGB')
        converted_result.save(os.path.expanduser('./output.jpg'))

