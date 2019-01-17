import static org.hamcrest.CoreMatchers.hasItems;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThat;
import static org.junit.Assert.assertTrue;

import java.util.Arrays;

import org.junit.Test;

public class EvenlyDivisibleTest {

	@Test
	public void primeFactorizationOf6() {
		assertEquals(Arrays.asList(2, 3), EvenlyDivisible.primeFactors(6));
		assertThat(EvenlyDivisible.primeFactors(6), hasItems(3, 2));
	}

	@Test
	public void primeFactorizationOf12() {
		assertEquals(Arrays.asList(2, 2, 3), EvenlyDivisible.primeFactors(12));
	}

	@Test
	public void primeFactorizationOf1() {
		assertTrue(EvenlyDivisible.primeFactors(1).isEmpty());
	}

	@Test
	public void primeFactorizationOf2() {
		assertEquals(Arrays.asList(2), EvenlyDivisible.primeFactors(2));
	}

	@Test
	public void primeFactorizationOf4() {
		assertEquals(Arrays.asList(2, 2), EvenlyDivisible.primeFactors(4));
	}

	@Test
	public void minDivisor_2_3_add_4() {
		assertEquals(Arrays.asList(2, 2, 3), EvenlyDivisible.minDivisors(Arrays.asList(2, 3), 4));
	}

	@Test
	public void minDivisor_2_2_3_add_5() {
		assertEquals(Arrays.asList(2, 2, 3, 5), EvenlyDivisible.minDivisors(Arrays.asList(2, 2, 3), 5));
	}

	@Test
	public void minDivisor_2_2_3_5_add_6() {
		assertEquals(Arrays.asList(2, 2, 3, 5), EvenlyDivisible.minDivisors(Arrays.asList(2, 2, 3, 5), 6));
	}

	@Test
	public void product_2_2_3_5_7() {
		assertEquals(420, EvenlyDivisible.product(Arrays.asList(2, 2, 3, 5, 7)));
	}

	@Test
	public void minDivisorOf1To10() {
		assertEquals(2520, EvenlyDivisible.minDivisorOf1ToN(10));
	}

	@Test
	public void minDivisorOf1To20() {
		assertEquals(232792560, EvenlyDivisible.minDivisorOf1ToN(20));
	}
}