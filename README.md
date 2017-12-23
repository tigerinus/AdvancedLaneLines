# Advanced Lane Finding Project

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.


---
Please see full code in the [IPython notebook](./AdvancedLaneLines.ipynb). Here's the [link to my video result](./project_video.mp4).


## Camera Calibration

*Briefly state how you computed the camera matrix and distortion coefficients. Provide an example of a distortion corrected calibration image.*

The code started with an array of object points for the grid. Then it goes thru each chessboard image in `camera_cal/calibration*.jpg` to find the chessboard corners by calling `cv2.findChessboardCorners(...)`. If found, it will collect both object points and the points of actual corners in the image. At the end it passes all object points and image points to `cv2.calibrateCamera(...)` and return whatever returned by that function.
