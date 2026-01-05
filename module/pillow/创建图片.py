from PIL import Image, ImageDraw, ImageFont


def create_img():
    img = Image.new('RGB', (500, 500), (255, 255, 255))
    with open('img.png', 'wb') as f:
        img.save(f, 'png')


def main():
    create_img()


if __name__ == '__main__':
    main()