from Cylinder import Cylinder
from Rectangle import Rectangle
from Circle import Circle

c = Circle(5)
c.CircleInfo()
print(f"")
c.radius = 5
c.CircleInfo()
print(f"-----------------")

r = Rectangle(6,8)
r.RectangleInfo()
print(f"")
r.width = 5
r.height = 10
r.RectangleInfo()
print(f"-----------------")

cy = Cylinder(8,9)
cy.CylinderInfo()
print(f"")
cy.radius = 5
cy.length = 10
cy.CylinderInfo()
print(f"-----------------")