from PIL import Image, ImageDraw, ImageFont

def draw_text():
    img = Image.new('RGB', (500, 500), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw.text([0,0],'python','red')
    img.save('pillow.png')


def main():
    draw_text()


if __name__ == '__main__':
    main()