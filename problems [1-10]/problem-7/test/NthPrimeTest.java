import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.util.Arrays;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class NthPrimeTest {

	@Test
	public void test2() {
		assertTrue(NthPrime.isPrime(2));
	}

	@Test
	public void test3() {
		assertTrue(NthPrime.isPrime(3));
	}

	@Test
	public void test4() {
		assertFalse(NthPrime.isPrime(4));
	}

	@Test
	public void test0() {
		assertFalse(NthPrime.isPrime(0));
	}

	@Test
	public void test11() {
		assertTrue(NthPrime.isPrime(11));
	}

	@Test
	public void test9() {
		assertFalse(NthPrime.isPrime(9));
	}

	@Test
	public void test1() {
		assertFalse(NthPrime.isPrime(1));
	}

	@Test
	public void test15485867() {
		assertTrue(NthPrime.isPrime(15485867));
	}

	// testing the generation of NthPrime

	@Test
	public void testGenerate0() {
		assertEquals(Arrays.asList(), NthPrime.generatePrime(0));
	}

	@Test
	public void testGenerate2() {
		assertEquals(Arrays.asList(2, 3), NthPrime.generatePrime(2));
	}

	@Test
	public void testGenerate3() {
		assertEquals(Arrays.asList(2, 3, 5), NthPrime.generatePrime(3));
	}

	@Test
	public void testGenerate5() {
		assertEquals(Arrays.asList(2, 3, 5, 7, 11), NthPrime.generatePrime(5));
	}

	// @formatter:off
	@Test
	public void testGenerate() {
		assertEquals(Arrays.asList(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
				83, 89), NthPrime.generatePrime(24));
	}

	// Testing the indexing of the list created by generateNthPrime

	@Test
	public void testIndex0() {
		assertEquals(Arrays.asList(), NthPrime.generatePrime(0));
	}

	@Test
	public void testIndex1() {
		assertEquals(2, NthPrime.indexPrime(1));
	}

	@Test
	public void testIndex2() {
		assertEquals(3, NthPrime.indexPrime(2));
	}

	@Test
	public void testIndex3() {
		assertEquals(5, NthPrime.indexPrime(3));
	}

	@Test
	public void testIndex5() {
		assertEquals(11, NthPrime.indexPrime(5));
	}

	@Test
	public void testIndex24() {
		assertEquals(89, NthPrime.indexPrime(24));
	}

	@Test
	public void testIndex10001() {
		assertEquals(104743, NthPrime.indexPrime(10001));
	}

}