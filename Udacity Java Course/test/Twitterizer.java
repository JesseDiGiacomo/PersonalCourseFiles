// Bluej project: twitter
//  TODO: Write code for the shorten(String longPost) method.
public class Twitterizer
{
    /**
     * Shortens and returns long posts by removing vowels
     * @param longPost the post whos vowels need to be removed
     * @return a version of the post without vowels
     */
    
    String longPost;
    String shortTweet;
    String letter;
    
    
    public String shorten(String longPost)
    {
        // YOUR CODE HERE
        shortTweet="";
        for (int i= 0; i<longPost.length(); i++)
        {
            letter = longPost.substring(i,i+1);
            if (!"aeiouAEIOU".contains(letter))
            {
                shortTweet = shortTweet + letter;
            }
        }
        return shortTweet;
    }
    
    public String reverse(String longPost)
    {
        String backwards = "";
        for (int i = longPost.length()-1; i >= 0; i--)
        {
            backwards = backwards + longPost.substring (i, i+1);
        }
        return backwards;
    }
}