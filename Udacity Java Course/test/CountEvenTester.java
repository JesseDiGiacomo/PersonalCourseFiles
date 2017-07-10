/**
 * Complete the class. Using a Scanner, ask the user to enter a series of integers with 
 * the following string "Enter an integer" and count the number of even numbers
 * Use a loop. Do not let bad input (a non-integer) terminate your program with an error.
 * When the user enters any non-integer, print the number of even integers entered and quit.
 * Hint: remember hasNextInt()
 * Hint: use the % operator to determine if a number is even
 */
import java.util.Scanner;
public class CountEvenTester
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int odd = 0;
        int even = 0;
        System.out.print("Enter an integer: ");
        
           while (in.hasNextInt())
           {
               int value = in.nextInt();
               if (value % 2 == 0)
               {
                   even++;
                   System.out.print("Enter an integer: ");
               }
               else
               {
                   odd++;
                   System.out.print("Enter an integer: ");
               }
               
           }
           System.out.println(even);
    }
}