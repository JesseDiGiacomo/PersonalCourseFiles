//Write a class Month.

//A Month has a constructor that takes the month number as a parameter (1 for January,
//2 for February and so forth):
//   public Month(int monthNumber)
//If monthNumber is not 1 to 12, set it to 1.  (This final case you can think of as
//a kind of safeguard against someone using your Month class incorrectly: even if
//someone passes a bad number to your constructor, it will still make a valid month.
//You will make a separate safeguard in your MonthPrinter class to reject bad user
//inputs, but making your code as resiliant as possible to incorrect usage is good
//practice as a programmer!)

//The Month class has 2 methods:
//   public String getMonthName() Use if / else if /else if ...
//   public int getNumberOfDays() Do NOT use a separate if / else branch for each month. 
//Use Boolean operators (&&, ||, !). You will have an if then else if then else
//For February return 28

//These are implemented for you as stubs

//Now write a class MonthPrinter which will instantiate a Month object, ask the user
//for a month number and print the name of the month and the number or days.

//If the month is 6, the output should look exactly like this:
//June 30

//If the user enters an invalid month number print this error message: 
//"Number must be 1 through 12"
//(We include this even though our Month constructor will gracefully handle improper
//inputs.  Using multiple safeguards against incorrect usage is a good idea!)

//If the user enters a non-integer, give this error message: 
//"Not an integer. Terminating"

//To be considered correct, you must enter the message exactly as specified, so be
//careful with the strings you print.

// Need help starting this question? In the lesson titled 
// "Starting points: Problem Set Questions", go to the
// problem titled "Problem Set 4 - Question 1" for some tips on 
// how to begin.

import java.util.Scanner;
public class Month
{
    //instance variables
    int monthNumber;
    String month;
    int numberOfDays;

    /**
     * Contructs a Month
     * @param the month number. Must be 1 to 12. For any other number, the month number is set to 1
     */
    public Month(int theMonthNumber)
    {
        //TODO: initialize the instance variable(s) to complete this constructor
        //Remember to make the constructor resiliant to improper inputs!
        monthNumber = theMonthNumber;
        if(monthNumber < 1 || monthNumber > 12)
           {
              monthNumber = 1;
           } 
           
    }

    /**
     * Gets the name of this month
     * @return the name of this month
     */
    public String getMonthName()
    {
        //TODO: implement this method (you will replace the return null statement below)
        if(monthNumber == 1)
    {
        month = "January";
    }
    else if(monthNumber == 2)
    {
        month = "February";
    }
    else if(monthNumber == 3)
    {
        month = "March";
    }
    else if(monthNumber == 4)
    {
        month = "April";
    }
    else if(monthNumber == 5)
    {
        month = "May";
    }
    else if(monthNumber == 6)
    {
        month = "June";
    }
    else if(monthNumber == 7)
    {
        month = "July";
    }
    else if(monthNumber == 8)
    {
        month = "August";
    }
    else if(monthNumber == 9)
    {
        month = "September";
    }
    else if(monthNumber == 10)
    {
        month = "October";
    }
    else if(monthNumber == 11)
    {
        month = "November";
    }
    else if(monthNumber == 12)
    {
        month = "December";
    }
    else 
    {
        System.out.println ("Number must be 1 through 12");
    }
    return month;
    }

    /**
     * Gets the number of days in this month
     * @return the number of days in this month in a non-leap year
     */
    public int getNumberOfDays()
    {
        //TODO: implement this method (you will replace the return 0 statement below)
        if(monthNumber == 2)
           {
               numberOfDays = 28;
           }
       else if (monthNumber == 4
                   || monthNumber == 6
                   || monthNumber == 9
                   || monthNumber == 11)
                        {
                            numberOfDays = 30;
                        }
        else
            {
                numberOfDays = 31;
            }
            return numberOfDays;
        
    }
}