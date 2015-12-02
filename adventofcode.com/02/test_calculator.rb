require 'minitest/autorun'
require_relative 'calculator'

class TestWrappingPaperCalculatorBean < MiniTest::Unit::TestCase
  def test_wrapping_calculation
    assert_equal 58, WrappingPaperCalculator.wrapping_paper_required(2, 3, 4)
    assert_equal 43, WrappingPaperCalculator.wrapping_paper_required(1, 1, 10)
  end

  def test_ribbon_calculation
    assert_equal 34, WrappingPaperCalculator.ribbon_required(2, 3, 4)
    assert_equal 14, WrappingPaperCalculator.ribbon_required(1, 1, 10)
  end
end
