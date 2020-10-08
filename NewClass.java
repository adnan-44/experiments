import java.util.*;
class NewClass {
	public static void main(String []args){
		System.out.println("Just for checking");
		Scanner in = new Scanner(System.in);
		int number = 0;
		while(true){
			System.out.println("Enter a number ");
			number = in.nextInt();
			if(number == 0){
				System.out.println("Done");
				break;
			}
			else{
				System.out.println("Typed "+number);
			}
		}
	}
}
