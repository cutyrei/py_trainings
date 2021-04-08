from PIL import Image, ImageFilter
image = Image.open('pro01.jpg')
#image.show()

# # rgb 변경
# r, g, b = image.split()
# convert_image = Image.merge("RGB", (b, g, r))
# convert_image.save('pro01_bgr.jpg')
# convert_image.show()


# # 흑백
# black_and_white = image.convert('1')
# black_and_white.save('pro01_bw.jpg')
# black_and_white.show()

# # 그레이스케일
# grey_img = image.convert("L")
# grey_img.save('pro01_greyscale.jpg')
# grey_img.show()

# # 회전/대칭
# image.rotate(90).show()
# image.transpose(Image.ROTATE_270).show() # transpose() 회전은 90/180/270 3가지만 가능
# image.crop((300,300,400,400)).show() # crop 인자는 tuple
# image.transpose(Image.FLIP_LEFT_RIGHT).show()
# image.transpose(Image.FLIP_TOP_BOTTOM).show()

# 필터
#image.filter(ImageFilter.GaussianBlur(5)).show() # GaussianBlur(), ImageFilter.BoxBlur()는 사용자 조정 가능, BLUR 는 조정 불가

filter_list = [ImageFilter.BLUR, ImageFilter.CONTOUR, ImageFilter.DETAIL, ImageFilter.EDGE_ENHANCE, ImageFilter.EDGE_ENHANCE_MORE, ImageFilter.EMBOSS, ImageFilter.FIND_EDGES,
            ImageFilter.SHARPEN, ImageFilter.SMOOTH, ImageFilter.SMOOTH_MORE]
for i in range(len(filter_list)):
    image.filter(filter_list[i]).show()
