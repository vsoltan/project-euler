package pe.triangularNumbers;

import java.util.ArrayList;
import java.util.List;

public class TriangularNumbers {
	public static List<Integer> generateFactors(int x) {
		List<Integer> factors = new ArrayList<Integer>();
		for (int i = 1; i <= x; ++i) {
			if (x % i == 0) {
				factors.add(i);
			}
		}
		return factors;
	}

	public static long generateNthTriangular(long n) {
		long triangularSum = 0;
		for (long i = 1; i <= n; ++i) {
			triangularSum += i;
		}
		return triangularSum;
	}

	// public static long triangularNFactor(long x,long f) {
	// for(x= 1; ++x;){
	// List<Integer> triangleFactor = generateFactors(x);
	// }

}
