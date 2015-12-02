require_relative 'calculator'
require_relative 'input'

paper_needed = INPUT.split("\n").map { |dimensions|
  dimensions = dimensions.split('x').map(&:to_i)
  WrappingPaperCalculator.wrapping_paper_required(*dimensions)
}.inject(&:+)

puts "paper: #{paper_needed}"
