public class StringDemo
{
    public static void main(String[] args)
    {
        String river = "Mississippi";
        river.replace ('i', 'x');
        System.out.println(river);
        int numberOfLetters = river.length();
        System.out.println(numberOfLetters);
    }
}