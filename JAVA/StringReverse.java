/*
* A basic java program to reverse the string 
*/

import java.util.Scanner;

class StringReverse{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the string: ");
    String string = sc.nextLine();
    char[] letters = string.toCharArray();    // convert string into char array

    // position variables to iterate over string
    int i = 0, j = string.length()-1;

    // Loop half of the string
    while(i < j){
      // In each iteration, swap the character, and increment the i and decrement the j value
      char temp = letters[i];
      letters[i] = letters[j];
      letters[j] = temp;

      i++;
      j--;
    }
    // Now convert the char array into string again
    string = String.valueOf(letters);

    // Output
    System.out.println(string);
  }
}