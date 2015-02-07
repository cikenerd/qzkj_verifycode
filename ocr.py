from PIL import Image
from chars_binary import chars
def identify(img):
	identification_code_temp=[];identification_code=['']*4;diff_min=[144]*4;
	for i in range (4):
		identification_code_temp.append(img.crop((i*10, 0, i*10+13, 12)).getdata())
	for char in chars:
		diff = [0]*4
		for i in range(4):
			for j in range(156):
				if identification_code_temp[i][j] ^ chars[char][j]:
						diff[i] += 1
		for i in range(4):
			if diff[i]<diff_min[i]:
				diff_min[i]=diff[i]
				identification_code[i]=char
	return ''.join(identification_code)

def identificationCodeHandle(img):
	rect_box = (3,4,46,16)	#crop rectangle,(left, upper, right, lower)
	img = img.crop(rect_box)
	img = img.convert('1')
	return img

if __name__=='__main__':
	for i in range(10):
		img = Image.open('verifycode/'+str(i)+'s.jpeg')
		img = identificationCodeHandle(img)
		identification_code = identify(img)
		print identification_code
