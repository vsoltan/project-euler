
public class Palindromic {
	public static boolean isPalindromic(long x) {
		String t = x + ""; // text representation of x
		String rt = new StringBuilder(t).reverse().toString(); // reverse t
		for (int i = 0; i < t.length() / 2; i++) {
			if (t.charAt(i) != rt.charAt(i)) {
				return false;
			}
		}
		return true;
	}

	public static long largestNthDigitNumber(int n) {
		long res = 0;
		for (int i = 0; i < n; i++) {
			res += 9 * (long) Math.pow(10, i);
		}
		return res;
	}

	public static long largestPalindromProductOfTwoNDigitNumbers(int n) {
		long maxNDigitNum = largestNthDigitNumber(n);
		long res = 0;
		System.out.println("Starting palindrom product: " + res);
		for (int x = 1; x <= maxNDigitNum; x++) {
			for (int y = 1; y <= maxNDigitNum; y++) {
				int x_dot_y = x * y;
				if (isPalindromic(x_dot_y)) {
					if (res < x_dot_y) {
						System.out.println("Largest palindrom product: " + x_dot_y + ", x=" + x + ", y=" + y);
					}
					res = Math.max(res, x_dot_y);
				}
			}
			System.out.print(".");
		}
		return res;
	}

	public static void main(String[] args) {
		System.out.println("LargestPalindromProductOfTwo3DigitNumbers: "
				+ Palindromic.largestPalindromProductOfTwoNDigitNumbers(3));

	}

}