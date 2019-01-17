
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class EvenlyDivisible {

	static List<Integer> primeFactors(int number) {
		int n = number;
		List<Integer> factors = new ArrayList<Integer>();
		for (int i = 2; i <= n / i; i++) {
			while (n % i == 0) {
				factors.add(i);
				n /= i;
			}
		}
		if (n > 1) {
			factors.add(n);
		}
		return factors;
	}

	/**
	 * Min list of factors for the divisors and a given number. E.g.
	 * 
	 * minDivisors([2, 3], 4) -> [2, 2, 3]
	 * 
	 * @param divisors
	 * @param number
	 * @return
	 */
	static List<Integer> minDivisors(List<Integer> divisors, int number) {
		List<Integer> primeFactors = primeFactors(number);
		List<Integer> result = new ArrayList<Integer>(divisors);
		List<Integer> currentDivisors = new ArrayList<Integer>(divisors);
		for (Integer factor : primeFactors) {
			if (!currentDivisors.remove(factor)) {
				result.add(factor);
			}
		}
		Collections.sort(result);
		return result;
	}

	static long product(List<Integer> factors) {
		return Arrays.stream(factors.toArray(new Integer[0])).reduce(1, (a, b) -> a * b);
	}

	static long minDivisorOf1ToN(Integer n) {
		List<Integer> factors = new ArrayList<Integer>();
		for (int i = 1; i <= n; i++) {
			factors = minDivisors(factors, i);
		}
		return product(factors);
	}

	public static void main(String args[]) {
		System.out.println(minDivisorOf1ToN(20));
	}
}