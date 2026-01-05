from PIL import Image, ImageDraw, ImageFont

def draw_line():
    img = Image.new('RGB', (500, 500), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw.line((100,100,100,300),fill='red')
    draw.line((100,100,300,100),fill='green')

    img.save('pillow.png')


def main():
    draw_line()


if __name__ == '__main__':
    main()