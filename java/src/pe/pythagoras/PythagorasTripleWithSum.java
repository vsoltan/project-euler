package pe.pythagoras;

public class PythagorasTripleWithSum {
	private long a, b, c;
	private final boolean valid;
	
	PythagorasTripleWithSum(long sum) {
		valid = compute(sum);
	}

	private boolean compute(long sum) {
		// Please add comments why /3 and /2
		for (a = 1; a < sum / 3; a++) {
			for (b = 1; b < sum / 2; b++) {
				c = sum - a - b;
				if (isPythagoreanTriple(a, b, c)) {
					return true;
				}
			}
		}
		return false;
	}

	static boolean isPythagoreanTriple(long a, long b, long c) {
		return a * a + b * b == c * c;
	}

	public long getA() {
		return a;
	}

	public long getB() {
		return b;
	}

	public long getC() {
		return c;
	}
	
	public boolean isValid() {
		return valid;
	}

	public static void main(String[] args) {
		PythagorasTripleWithSum pythagoras = new PythagorasTripleWithSum(1000);
		long a = pythagoras.getA();
		long b = pythagoras.getB();
		long c = pythagoras.getC();
		System.out.println("a=" + a + ", b=" + b + ", c=" + c + " : a triple whose product equals to: " + a * b * c);
	}
}
