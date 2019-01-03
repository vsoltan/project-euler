package pe.primes;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.util.Arrays;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class PrimesTest {

	@Test
	public void test2() {
		assertTrue(Primes.isPrime(2));
	}

	@Test
	public void test3() {
		assertTrue(Primes.isPrime(3));
	}

	@Test
	public void test4() {
		assertFalse(Primes.isPrime(4));
	}

	@Test
	public void test0() {
		assertFalse(Primes.isPrime(0));
	}

	@Test
	public void test11() {
		assertTrue(Primes.isPrime(11));
	}

	@Test
	public void test9() {
		assertFalse(Primes.isPrime(9));
	}

	@Test
	public void test1() {
		assertFalse(Primes.isPrime(1));
	}

	@Test
	public void test15485867() {
		assertTrue(Primes.isPrime(15485867));
	}

	// testing the generation of primes

	@Test
	public void testGenerate0() {
		assertEquals(Arrays.asList(), Primes.generatePrime(0));
	}

	@Test
	public void testGenerate2() {
		assertEquals(Arrays.asList(2, 3), Primes.generatePrime(2));
	}

	@Test
	public void testGenerate3() {
		assertEquals(Arrays.asList(2, 3, 5), Primes.generatePrime(3));
	}

	@Test
	public void testGenerate5() {
		assertEquals(Arrays.asList(2, 3, 5, 7, 11), Primes.generatePrime(5));
	}
	// @formatter:off
	@Test
	public void testGenerate() {
		assertEquals(Arrays.asList(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
				59, 61, 67, 71, 73, 79, 83, 89), Primes.generatePrime(24));
	}

	// Testing the indexing of the list created by generatePrimes

	@Test
	public void testIndex0() {
		assertEquals(Arrays.asList(), Primes.generatePrime(0));
	}

	@Test
	public void testIndex1() {
		assertEquals(2, Primes.indexPrime(1));
	}

	@Test
	public void testIndex2() {
		assertEquals(3, Primes.indexPrime(2));
	}

	@Test
	public void testIndex3() {
		assertEquals(5, Primes.indexPrime(3));
	}

	@Test
	public void testIndex5() {
		assertEquals(11, Primes.indexPrime(5));
	}

	@Test
	public void testIndex24() {
		assertEquals(89, Primes.indexPrime(24));
	}

	@Test
	public void testIndex10001() {
		assertEquals(104743, Primes.indexPrime(10001));
	}

}
