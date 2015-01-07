# converts docker style environment variable declaration
# ('-e SECRET_KEY foo') to shell style (SECRET_KEY=foo).

while line = gets
  # key, value = line.strip.split('-e')
  puts <<DOC
  # key, value
DOC
end

