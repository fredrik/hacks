while line = gets
  name, value = line.strip.split('=')
  puts <<DOC
{
  "name": "#{name}",
  "value": "#{value}"
},
DOC
end
