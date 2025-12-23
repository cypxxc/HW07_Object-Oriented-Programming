namespace HW07
{
    class Rectangle{
        public double Width { get; set; } = 1.0;
        public double Height { get; set; } = 1.0;

        public double Area => Width * Height;

        public void RectangleInfo(){
            System.Console.WriteLine($"Width: {Width:N2}");
            System.Console.WriteLine($"Height: {Height:N2}");
            System.Console.WriteLine($"Area: {Area:N2}");
        }
    }
}