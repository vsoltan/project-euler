import java.util.ArrayList;
import java.util.List;

public class NthPrime {

	public static boolean isPrime(int number) {
		if (number == 0 || number == 1) {
			return false;
		}
		for (int i = 2; i < (number); ++i) {
			if (number % i == 0) {
				return false;
			}
		}
		return true;
	}

	static List<Integer> generatePrime(int range) {
		List<Integer> Primes = new ArrayList<Integer>();
		for (int i = 2; Primes.size() < range; ++i) {
			if (isPrime(i) == true) {
				Primes.add(i);
			}
		}
		return Primes;

	}

	static int indexPrime(int numberPrime) {
		List<Integer> Primes = new ArrayList<Integer>(generatePrime(numberPrime));
		return Primes.get(numberPrime - 1);

	}

	public static void main(String[] args) {
		System.out.println(indexPrime(10001));
	}
}
