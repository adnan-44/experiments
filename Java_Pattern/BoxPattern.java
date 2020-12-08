import java.util.Scanner;
class BoxPattern{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter side for pattern: ");
    int n = sc.nextInt();
    System.out.println();

    //Pattern code
    //outer loop for repeating inner loop
    for(int i=0; i<n; i++){

      //inner loop for printing */#
      for(int j=0; j<n; j++){
        System.out.print("* ");
      }

      //line break after every line
      System.out.println();
    }
  }
}
