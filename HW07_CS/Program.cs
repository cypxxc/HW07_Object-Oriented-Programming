using HW07;

var c = new Circle();
c.CircleInfo();
var c2 = new Circle{Radius = 5.5};
c2.CircleInfo();

System.Console.WriteLine("");
c.Radius = 5;
c.CircleInfo();
System.Console.WriteLine("-----------------");

var r = new Rectangle{Width = 5, Height = 10};
r.RectangleInfo();
System.Console.WriteLine("");
r.Width = 5;
r.Height = 10;
r.RectangleInfo();
System.Console.WriteLine("-----------------");

var cy = new Cylinder { Radius = 5, Length = 10};
cy.CylinderInfo();
System.Console.WriteLine("");
cy.Radius = 5;
cy.Length = 10;
cy.CylinderInfo();
System.Console.WriteLine("-----------------");
