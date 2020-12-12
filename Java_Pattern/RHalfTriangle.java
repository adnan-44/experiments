import java.util.Scanner;

class RHalfTriangle{

  public static void main(String[] args){
    //for input
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter number: ");
    int n = sc.nextInt();
    System.out.println();

    //outer loop for row
    for(int i=1; i <= n; i++){

      // prints space until j value less than i-1
      for(int j=1; j <= i-1; j++){
        System.out.print("  ");
      }

      // * prints until j value less than n-i+1
      for(int j=1; j <= n-i+1; j++){
        System.out.print("* ");
      }

      //line break once j equals n-i+1 value
      System.out.println();
    }
  }
}
