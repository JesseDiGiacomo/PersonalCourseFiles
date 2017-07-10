public class CountryNames
{
    /**
     * Gets the name with the proper article
     * @param name the country name
     * @return the name prepended with the proper article
     */
    public String getCompleteName(String name)
    {

         //your code goes here
        String countryName = name;
        String first = countryName.substring(0, 1);
        String last = countryName.substring(countryName.length() - 1);
        if (!last.equals("e") ||
        	   countryName.equals("Belize") ||
            countryName.equals("Cambodge") ||
            countryName.equals("Mexique") ||
            countryName.equals("Mozambique") ||
            countryName.equals("Zaire") ||
            countryName.equals("Zimbabwe"))
        {
            if (countryName.equals("Etats-Unis") ||
                 countryName.equals("Pays-Bas"))
                {
                    countryName = "les " + name;
                }
            else
            {
                countryName = "le " + name;
            }
        }
        else if (first.equals("A") ||
                 first.equals("E") ||
                 first.equals("I") ||
                 first.equals("O") ||
                 first.equals("U"))
        {
            countryName = "l'" + name;
        } 
        else
        {
            countryName = "la " + name;
        }      
        return countryName;
    }
}