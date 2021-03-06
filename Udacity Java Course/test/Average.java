// Bluej project: lesson6/average_q
// TODO: Update your method average() so that it can accept
// altitudes (which can be positive, negative or zero).
// Use Q as a sentinel value instead of 0.
// Use the scanner method hasNextDouble to control your loop.
// Remember to change the prompt.

import java.util.Scanner;

public class Average
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        double value;
        int count = 0;
        double sum = 0;
        boolean done = false;

        while (!done)
        {
            System.out.print("Enter a value, Q to quit: ");
            
            if (in.hasNextDouble())
            {
                value = in.nextDouble();
                sum = sum + value;
                count++;
            }
            else
            {
                done = true;

            }
        }
        double average = sum / count;
        if (count == 0)
        {
            System.out.println ("Error: No input");
        }
        else
        {
            System.out.printf("Average: %.2f\n", average);
        }
        
    }
}