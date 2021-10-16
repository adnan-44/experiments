/*
* A basic java program to check whether given string is an Palindrome or not.
* A string which is same after reversing is known as Palindrome string.
*/

import java.util.Scanner;

class Palindrome{

  public static boolean isPalindrome(String string){
    boolean isPalin = true;   // Let's say string is palindrome by default

    // Position variables to iterate over string
    int i = 0, j = string.length()-1;

    // Now iterate half of the string, because if string is palindrome then other half will be same as first
    while(i < j){
      // Check character their opposite location, they should be same if string is palindrome
      if(string.charAt(i) != string.charAt(j)){
        isPalin = false;
        break;
      }

      // Increment i and decrement j by 1 to iterate the string
      i++;
      j--;
    }

    return isPalin;   // Return the result
  }
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the string: ");
    String string = sc.nextLine();
    
    // Output
    System.out.println(isPalindrome(string));
  }
}