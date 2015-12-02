class WrappingPaperCalculator
  def self.wrapping_paper_required(length, width, height)
    sides = [length*width, width*height, height*length]
    sides.map {|s| 2*s }.inject(&:+) + sides.sort.first
  end

  def self.ribbon_required(length, width, height)
    perimeters = [(length+width)*2, (width+height)*2, (height+length)*2]
    perimeters.sort.first + length*width*height
  end
end
