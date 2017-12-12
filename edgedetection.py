import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# Read in an image and grayscale it
#image = mpimg.imread('images\\test.jpg')
image = mpimg.imread('images\\center.jpg')

# Define a function that applies Sobel x or y, 
# then takes an absolute value and applies a threshold.
# Note: calling your function with orient='x', thresh_min=5, thresh_max=100
# should produce output like the example image shown above this quiz.
def abs_sobel_thresh(img, orient,  sobel_kernel, thresh):
    
    # Apply the following steps to img
    img = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    img = img[:,:,2]
    
    # 2) Take the derivative in x or y given orient = 'x' or 'y'
    x = 1
    y = 0
    
    if orient == 'y':
        x = 0
        y = 1
    
    img = cv2.Sobel(img,cv2.CV_64F,x,y,ksize=sobel_kernel)
    # 3) Take the absolute value of the derivative or gradient
    
    img = np.absolute(img)
    # 4) Scale to 8-bit (0 - 255) then convert to type = np.uint8
    
    img = np.uint8(255 * img / np.max(img))


    # 5) Create a mask of 1's where the scaled gradient magnitude 
            # is > thresh_min and < thresh_max
    binary_output = np.zeros_like(img)
    binary_output[(img >= thresh[0]) & (img <= thresh[1])] = 1
    return binary_output

def mag_thresh(img, sobel_kernel=3, mag_thresh=(0, 255)):
    
    # Apply the following steps to img
    img = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    img = img[:,:,2]

    # 2) Take the gradient in x and y separately
    img_x = cv2.Sobel(img,cv2.CV_64F,1,0, ksize=sobel_kernel)
    img_y = cv2.Sobel(img,cv2.CV_64F,0,1, ksize=sobel_kernel)
    
    # 3) Calculate the magnitude 
    img = np.sqrt(img_x**2 + img_y**2)
    
    # 4) Scale to 8-bit (0 - 255) and convert to type = np.uint8
    img = np.uint8(255 * img / np.max(img))
    
    # 5) Create a binary mask where mag thresholds are met

    # 6) Return this mask as your binary_output image
    binary_output = np.zeros_like(img)
    binary_output[(img >= mag_thresh[0]) & (img <= mag_thresh[1])] = 1
    return binary_output

def dir_threshold(img, sobel_kernel=3, thresh=(0, np.pi/2)):
    
    # Apply the following steps to img
    img = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    img = img[:,:,2]

    # 2) Take the gradient in x and y separately
    img_x = cv2.Sobel(img,cv2.CV_64F,1,0, ksize=sobel_kernel)
    img_y = cv2.Sobel(img,cv2.CV_64F,0,1, ksize=sobel_kernel)
    
    # 3) Take the absolute value of the x and y gradients
    img_x = np.absolute(img_x)
    img_y = np.absolute(img_y)
    
    # 4) Use np.arctan2(abs_sobely, abs_sobelx) to calculate the direction of the gradient 
    img = np.arctan2(img_y, img_x)
    
    # 5) Create a binary mask where direction thresholds are met
    # 6) Return this mask as your binary_output image
    
    binary_output = np.zeros_like(img)
    binary_output[(img >= thresh[0]) & (img <= thresh[1])] = 1
    
    return binary_output


# Run the function
ksize = 5

gradx = abs_sobel_thresh(image, orient='x', sobel_kernel=ksize, thresh=(10, 255))
grady = abs_sobel_thresh(image, orient='y', sobel_kernel=ksize, thresh=(40, 255))

combined_grad = np.zeros_like(gradx)
combined_grad[(gradx == 1) & (grady == 1)] = 1

mag_binary = mag_thresh(image, sobel_kernel=ksize, mag_thresh=(40, 255))
dir_binary = dir_threshold(image, sobel_kernel=ksize, thresh=(0.6, 1.4))

combined_binary = np.zeros_like(mag_binary)
combined_binary[(mag_binary == 1) & (dir_binary == 1)] = 1

combined = np.zeros_like(dir_binary)
combined[(combined_grad == 1) & (combined_binary == 1)] = 1

color_binary = np.dstack(( np.zeros_like(combined), combined_grad, combined_binary))


# Plot the result
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
f.tight_layout()
ax1.imshow(image)
ax1.set_title('Original Image', fontsize=50)
ax2.imshow(color_binary)
ax2.set_title('Output', fontsize=50)
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)

plt.show()