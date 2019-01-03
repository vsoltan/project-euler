package pe.palindromic;
import static org.junit.Assert.*;

import org.junit.Test;

public class PalindromicTest {

	@Test
	public void zeroShouldBePalindromic() {
		assertTrue(Palindromic.isPalindromic(0));
	}

	@Test
	public void evenDigitsShouldBePalindromic() {
		assertTrue(Palindromic.isPalindromic(11));
	}

	@Test
	public void oddDigitsShouldBePalindromic() {
		assertTrue(Palindromic.isPalindromic(232));
	}

	@Test
	public void longOddPalindromic() {
		assertTrue(Palindromic.isPalindromic(21312));
	}

	@Test
	public void evenDigitsNonPalindromic() {
		assertFalse(Palindromic.isPalindromic(23));
	}

	@Test
	public void oddDigitsNonPalindromic() {
		assertFalse(Palindromic.isPalindromic(231));
	}

	@Test
	public void longOddNonPalindromic() {
		assertFalse(Palindromic.isPalindromic(1213321));
	}

	@Test
	public void longEvenNonPalindromic() {
		assertTrue(Palindromic.isPalindromic(12133121));
	}

	@Test
	public void largest1DigitNumber() {
		assertEquals(9, Palindromic.largestNthDigitNumber(1));
	}
	
	@Test
	public void largest2DigitNumber() {
		assertEquals(99, Palindromic.largestNthDigitNumber(2));
	}
	
	@Test
	public void largest3DigitNumber() {
		assertEquals(999, Palindromic.largestNthDigitNumber(3));
	}
	
	@Test
	public void largestPalindromProductOfTwo2DigitNumbers() {
		assertEquals(9009, Palindromic.largestPalindromProductOfTwoNDigitNumbers(2));
	}
	
}
