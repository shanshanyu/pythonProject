from PIL import Image, ImageDraw, ImageFont

def draw_point():
    # 先创建一个图片
    img = Image.new('RGB', (500, 500), (255, 255, 255))
    # 创建ImageDraw对象
    draw = ImageDraw.Draw(img)

    draw.point([100,100],fill='red')
    draw.point([200,200],fill='green')
    img.save('code.png')


def main():
    draw_point()


if __name__ == '__main__':
    main()