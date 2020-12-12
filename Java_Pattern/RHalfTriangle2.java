import java.util.Scanner;

class RHalfTriangle2{

  public static void main(String[] args){
    //for input
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter number: ");
    int n = sc.nextInt();
    System.out.println();

    //outer loop for row
    for(int i=1; i <= n; i++){

      // prints space until j value less than n-1
      for(int j=1; j <= n-i; j++){
        System.out.print("  ");
      }

      // * prints until j value less than i
      for(int j=1; j <= i; j++){
        System.out.print("* ");
      }

      //line break once j equals i value
      System.out.println();
    }
  }
}
