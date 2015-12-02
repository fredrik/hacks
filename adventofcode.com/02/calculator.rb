class WrappingPaperCalculator
  def self.wrapping_paper_required(length, width, height)
    sides = [length*width, width*height, height*length]
    sides.map {|s| 2*s }.inject(&:+) + sides.sort.first
  end
end
