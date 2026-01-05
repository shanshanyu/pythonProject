from PIL import Image, ImageDraw, ImageFont


def draw_circle():
    img = Image.new('RGB', (500, 500), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # 第一个参数：表示起始坐标和结束坐标（圆要画在其中间）
    # 第二个参数：表示开始角度
    # 第三个参数：表示结束角度
    # 第四个参数：表示颜色
    draw.arc((100,100,300,300),0,360,fill='red')
    img.save('circle.png')


def main():
    draw_circle()


if __name__ == '__main__':
    main()