from PIL import Image
rect_box = (3,4,46,16)	#crop rectangle,(left, upper, right, lower)
chars=('1','2','3','z','x','c','v','b','n','m') #identification_code only have these characters
def identify(img):
	identification_code_temp=[];identification_code=['']*4;diff_min=[144]*4;
	for i in range (4):
		identification_code_temp.append(img.crop((i*10, 0, i*10+13, 12)))
	for char in chars:
		diff = [0]*4
		char_temp = Image.open('char_template/'+str(char)+'.jpeg').convert('L')
		for x in range(12):
			for y in range(12):
				for i in range(4):
					xy=(x,y)
					if identification_code_temp[i].getpixel(xy) ^ char_temp.getpixel(xy)>128:	#if the two pixel color is different
						diff[i] += 1
		for i in range(4):
			if diff[i]<diff_min[i]:
				diff_min[i]=diff[i]
				identification_code[i]=char
	return ''.join(identification_code)

def identificationCodeHandle(img):
	img = img.crop(rect_box)
	for x in range(43):
		for y in range(12):
			xy=(x, y)
			if sum(img.getpixel(xy))>333:
				img.putpixel(xy, (255, 255, 255))
	img = img.convert(mode='L')
	return img

if __name__=='__main__':
	for i in range(10):
		img = Image.open('verifycode/'+str(i)+'s.jpeg')
		img = identificationCodeHandle(img)
		identification_code = identify(img)
		print identification_code
