"""Виртуальный прокси. Продолжаем следовать принципу открытости-закрытости.
Чтобы не загружать картинку, пока не вызван метод draw, мы создаем подкласс
 прокси LazyBitmap, который инициалиизирует класс Bitmap, только если вызван метод draw."""

class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f'Loading image from {filename}')

    def draw(self):
        print(f'Drawing image {self.filename}')


class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self.bitmap = None

    def draw(self):
        if not self.bitmap:
            self.bitmap = Bitmap(self.filename)
        self.bitmap.draw()

def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done drawing image')

if __name__ == '__main__':
    bmp = LazyBitmap('facepalm.jpg')  # Bitmap
    draw_image(bmp)
