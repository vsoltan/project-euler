package pe.pythagoras;
import static org.junit.Assert.*;

import org.junit.Test;

public class PythagorasTripleWithSumTest {
	
	@Test
	public void twelveIsValid() {
		assertTrue(new PythagorasTripleWithSum(12).isValid());
	}

	@Test
	public void twelveShouldCompute_3_4_5() {
		PythagorasTripleWithSum p = new PythagorasTripleWithSum(12);
		assertEquals(3, p.getA());
		assertEquals(4, p.getB());
		assertEquals(5, p.getC());
	}

	@Test
	public void thirtyIsValid() {
		assertTrue(new PythagorasTripleWithSum(30).isValid());
	}

	@Test
	public void thirtyShouldCompute_5_12_13() {
		PythagorasTripleWithSum p = new PythagorasTripleWithSum(30);
		assertEquals(5, p.getA());
		assertEquals(12, p.getB());
		assertEquals(13, p.getC());
	}

	@Test
	public void thousandIsValid() {
		assertTrue(new PythagorasTripleWithSum(1000).isValid());
	}

	@Test
	public void thousandShouldCompute_200_375_425() {
		PythagorasTripleWithSum p = new PythagorasTripleWithSum(1000);
		assertEquals(200, p.getA());
		assertEquals(375, p.getB());
		assertEquals(425, p.getC());
	}

	@Test
	public void isPythegorreanTriple_3_4_5() {
		assertTrue(PythagorasTripleWithSum.isPythagoreanTriple(3, 4, 5));
	}

	@Test
	public void isNotPythegorreanTriple_3_4_6() {
		assertFalse(PythagorasTripleWithSum.isPythagoreanTriple(3, 4, 6));
	}

	@Test
	public void isPythegorreanTriple_5_12_13() {
		assertTrue(PythagorasTripleWithSum.isPythagoreanTriple(5, 12, 13));
	}

	@Test
	public void isNotPythegorreanTriple_5_11_13() {
		assertFalse(PythagorasTripleWithSum.isPythagoreanTriple(5, 11, 13));
	}

	@Test
	public void isPythegorreanTriple_200_375_425() {
		assertTrue(PythagorasTripleWithSum.isPythagoreanTriple(200, 375, 425));
	}

	@Test
	public void isNotPythegorreanTriple_199_375_425() {
		assertFalse(PythagorasTripleWithSum.isPythagoreanTriple(199, 375, 425));
	}

}