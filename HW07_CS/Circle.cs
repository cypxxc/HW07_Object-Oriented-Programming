namespace HW07
{
    class Circle{
        public double Radius { get; set; } = 1.0;

        public double Area => Math.PI * Math.Pow(Radius, 2);
        
        public void CircleInfo(){
            System.Console.WriteLine($"Radius: {Radius:N2}");
            System.Console.WriteLine($"Area: {Area:N2}");
        }
    }
}