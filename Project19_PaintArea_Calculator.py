## Project 19: Paint Area Calculator
##Find how many cans of paint is required to paint a given surface area.
## one can of paint can cover 5 square meters.Given a random height and width of the wall and find out how many cns of paint is required.

def paint_req(height, width,One_can_paint):
    Area_of_wall=height*width
    #One_can_paint = 5
    Paint_cans_req= round(Area_of_wall/One_can_paint)
    print(f"For wall of height {height}m and width of {width}m , you need {Paint_cans_req} cans of paint.")





ht=int(input("Enter the height of the wall in meters:"))
width=int(input("Enter the width of the wall in meters:"))
Paint_capacity=int(input("How much area each paint container can cover: "))
paint_req(height=ht,width=width,One_can_paint=Paint_capacity)


