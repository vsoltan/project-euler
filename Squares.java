public class Squares{
	public static int addSquares(int n){
		int k, sum = 0;
		for(k = 1; k <= n; k++);
		sum+= k*k;
		return sum;
	}
	public static void main(String [] args){
		System.out.println(addSquares(5));
	}
}