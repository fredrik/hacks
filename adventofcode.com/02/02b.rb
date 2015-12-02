require_relative 'calculator'
require_relative 'input'

ribbon_needed = INPUT.split("\n").map { |dimensions|
  dimensions = dimensions.split('x').map(&:to_i)
  WrappingPaperCalculator.ribbon_required(*dimensions)
}.inject(&:+)

puts "ribbon: #{ribbon_needed}"
