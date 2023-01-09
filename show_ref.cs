using System;
class MyClass
{
    public unsafe void PrintInfo(int myInt, string prompt)
    {
        int* ptrMyInt = &myInt;
        Console.WriteLine(prompt);
        Console.WriteLine("{0}{1} {2}    {3} {4}",
            nameof(myInt), "值：", myInt, "位址：", (int)ptrMyInt);
        Console.WriteLine();
    }
}

class MyClient
{
    public static void Main()
    {
        MyClass myClass = new MyClass();
        int i = 3;
        myClass.PrintInfo(i, "Before change");
        i = 5;
        myClass.PrintInfo(i, "After change");
        // Console.ReadLine();
    }
}