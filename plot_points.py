from turtle import distance
from scipy.spatial import distance as dist
import cv2
import sys

import csv
current_line_number = 2

point1 = None
point2 = None


scale_point_1 = None
scale_point_2 = None
fixed_distance = None
fixed_distance_on_image = None
f = None
image = None
factor = 1.0


def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

def plot_point(x, y):
    global image
    image = cv2.circle(image, (x,y), radius=0, color=(0, 0, 255), thickness=5)

def plot_line(p1, p2):
    global image
    x1, y1 = p1
    x2, y2 = p2
    image = cv2.line(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 1)


headers = ["Row", "X1", "Y1", "X2", "Y2", "Distance"]
f = open("templates/Outputs/Distance_data.csv", "w")
writer = csv.writer(f)
writer.writerow(headers)

def myMouseHandler(event,x,y,flags,param):
    global point1, point2
    global scale_point_1, scale_point_2
    global image
    global fixed_distance_on_image, fixed_distance_on_image_cm, current_line_number, f

    
    

    if event == cv2.EVENT_LBUTTONDOWN:
        if (not scale_point_1) and (not scale_point_2) and (not point1) and (not point2):
            scale_point_1 = [x, y]
            plot_point(x, y)
        
        elif (scale_point_1) and (not scale_point_2):
            scale_point_2 = [x, y]
            plot_point(x, y)
            plot_line(scale_point_1, scale_point_2)
            fixed_distance_on_image = dist.euclidean(scale_point_1, scale_point_2)
            fixed_distance_on_image_cm = 0.02648 * fixed_distance_on_image

            (mX, mY) = midpoint(scale_point_1, scale_point_2)
            cv2.putText(image, "{:.10f} cm".format(fixed_distance_on_image_cm), (int(mX), int(mY - 10)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
        
        elif (scale_point_1) and (scale_point_2) and (not point1) and (not point2):
            point1 = [x, y]
            plot_point(x, y)
        
        elif (scale_point_1) and (scale_point_2) and (point1) and (not point2):
            point2 = [x, y]
            plot_point(x, y)
            plot_line(point1, point2)
            (mX, mY) = midpoint(point1, point2)

            dist_on_image = dist.euclidean(point1, point2) * 0.02648
            actual_distance = dist_on_image * (fixed_distance / fixed_distance_on_image_cm)

            cv2.putText(image, "{:.10f} cm".format(actual_distance), (int(mX), int(mY - 10)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
            print("Second point plotted")
            writer.writerow([
                current_line_number - 1,
                point1[0], point1[1], point2[0], point2[1], actual_distance]
            )
            current_line_number += 1
            point1 = point2 = None
    
    # f.close()

print(sys.argv)

# fixed_distance = float(input("Fixed distance (in cm) = "))
fixed_distance = float(sys.argv[1])
image_path = sys.argv[2]
cv2.namedWindow("window")
image = cv2.imread(image_path)
cv2.setMouseCallback("window", myMouseHandler)



while True:
    # both windows are displaying the same img
    cv2.imshow("window", image)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        f.close()
        break

cv2.destroyAllWindows()
