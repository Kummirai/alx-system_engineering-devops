#!/usr/bin/env ruby
#Regular expression that is matches 10 digit phone number
puts ARGV[0].scan(/^[0-9]{10}$/).join
