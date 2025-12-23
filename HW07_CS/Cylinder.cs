namespace HW07
{
    class Cylinder{
        public double Radius { get; set; } = 1.0;
        public double Length { get; set; } = 1.0;

        public double Area => 2 * Math.PI * Radius * (Radius + Length);

        public double Volume => Area * Length;

        public void CylinderInfo(){
            System.Console.WriteLine($"Radius: {Radius:N2}");
            System.Console.WriteLine($"Length: {Length:N2}");
            System.Console.WriteLine($"Area: {Area:N2}");
            System.Console.WriteLine($"Volume: {Volume:N2}");
        }
    }
}