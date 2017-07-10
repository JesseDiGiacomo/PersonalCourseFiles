
public class CreditCard
{
    private long cardNumber;

    public CreditCard(long cardNumber)
    {
        this.cardNumber = cardNumber;
    }
    
    /**
     * Calculates whether this CreditCard has a valid number.
     * @return true if the number is valid, false if it's not.
     */
    public boolean isValid()
    {
        /* Pseudocode for isValid:
         * sum = 0
         * count = 0
         * for each digit starting from the right
         *     count ++
         *     if count is odd
         *         sum = sum + digit
         *     else if (digit < 5)
         *         sum = sum + 2 * digit
         *     else
         *         sum = sum + 2 * digit - 9
         * if the last digit of the sum is zero
         *     The card number is valid
         */
        long n = cardNumber;
        int sum = 0;
        int count = 0;

        // TODO this is the code from the last question. you can use it
        // as a starting point, but you will need to change most of it.
        while (n > 0)
        {
            count ++;
            int digit = (int)(n % 10);
            if (count % 2 == 1){
                sum = sum + digit;
            }
            else if (digit <5)
            {
                sum = sum + 2 * digit;
            }
            else {
                sum = sum + 2 * digit - 9;
            }
            n = n/10;
        }
        
        return sum % 10 == 0;
    }

    /**
     * Calculates the sum of ever other digit in cardNumber 
     * starting from the rightmost digit.
     * @return the sum of every other digit starting from the rightmost.
     */
    public int sumCertainDigits()
    {
        // So that we don't accidentally change the credit card number,
        // make a copy called n. 
        long n = cardNumber;
        
        // TODO this is the code from the a previous video. You can use it
        // as a starting point, but you will need to change a lot.
        // Change this method so that it will calculate the sum of every
        // second digit instead of all the digits, and then return this 
        // special sum. 
        // for example, if n is 12345, this method should return the sum 
        // 5 + 3 + 1
        // There are links to videos with hints above the submit button. 
        // Use them if you want more inspiration.
        int sum = 0;
        int count = 0;
        
        while (n > 0)
        {
            count ++;
            int digit = (int)(n % 10); 
            if (count % 2 == 1){
                sum = sum + digit;
            }
            n = n/10;
        }
        return sum;
    }
}
